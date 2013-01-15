import csvio
import sys
import re

def normalize(value):
  return value.strip()

def process(routes):
  csvio.transform(routes,'route_short_name',normalize)
  csvio.transform(routes,'route_long_name',normalize)
  for route in routes:
    short_name = route['route_short_name']
    if re.match(r'^\d+$',short_name):
      continue
    long_name = route['route_long_name']
    if long_name:
      m = re.search(r'^([^-]+)\s*-\s*(\d+)$',long_name)
      if m:
        route['route_short_name'] = m.group(2)
        route['route_long_name'] = m.group(1)
        continue
    if short_name == 'St. Charles':
      if long_name == 'Shuttle':
        route['route_short_name'] = '13'
        route['route_long_name'] = 'St. Charles Shuttle'
        continue
      else:
        route['route_short_name'] = '12'
        route['route_long_name'] = 'St. Charles'
        continue
    if short_name == 'Riverfront':
      route['route_short_name'] = '2'
      route['route_long_name'] = 'Riverfront'
      continue
    if short_name == 'Loyola-UPT':
      route['route_short_name'] = '49'
      route['route_long_name'] = 'Loyola-UPT'
      continue
  return routes

if __name__ == '__main__':
  datadir = sys.argv[1]
  routes = csvio.read('%s/routes.txt' % datadir)
  routes = process(routes)
  csvio.write('%s/routes.txt' % datadir,routes)
