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
    long_name = route['route_long_name']

    # if the short name is a number then we are good
    if re.match(r'^\d+$',short_name):
      continue

    if long_name:
      m = re.search(r'^([^-]+)\s*-\s*(\d+)$',long_name)
      if m:
        route['route_short_name'] = m.group(2)
        route['route_long_name'] = m.group(1)
        continue
    if short_name == '47 Cemeteries':
        route['route_short_name'] = '47'
        continue
    if short_name == '48 City Park':
        route['route_short_name'] = '48'
        continue
    if short_name == '12B St. Charles':
        route['route_short_name'] = '12'
        continue
    if short_name == 'F': # algiers point ferry
        # give this a synthetic short name just so everything works
        route['route_short_name'] = '1001'
        continue
    if re.match(r'(12\s+)?St. Charles',short_name):
        route['route_short_name'] = '12'
        if not long_name:
          if route['route_type'] == '3':
            route['route_long_name'] = 'St. Charles Shuttle'
          else:
            route['route_long_name'] = 'St. Charles Streetcar'            
        continue
    if re.match(r'(2\s+)?Riverfront',short_name):
      route['route_short_name'] = '2'
      route['route_long_name'] = 'Riverfront'
      continue
    if re.match(r'(49\s+)?Loyola-UPT',short_name):
      route['route_short_name'] = '49'
      route['route_long_name'] = 'Loyola-UPT'
      continue

    print "No route code for route_id=%(route_id)s short_name=%(route_short_name)s long_name=%(route_long_name)s" % route

  for route in routes:
    code = int(route['route_short_name'])
  return routes

if __name__ == '__main__':
  datadir = sys.argv[1]
  routes = csvio.read('%s/routes.txt' % datadir)
  routes = process(routes)
  csvio.write('%s/routes.txt' % datadir,routes)
