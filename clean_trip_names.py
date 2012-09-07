import csvio
import sys
import re

# This cleans up trip names and tries to regularize them as much as possible

def normalize(name):
  name = name.strip()
  # remove duplicate spaces
  name = re.sub(r'\s+',' ',name)
  return name

def process(routes,trips):
  csvio.transform(trips,'trip_headsign',normalize)

  # encode the route and direction into the trip-id. 
  # OTP returns the trip_id in the plan results, and this lets us get access
  # to the route and the direction which we would otherwise not be able to do

  # the "route" here i refer to is really the code/number - which we've ensured
  # already is in route.route_short_name
  route_code_by_id = {}
  for r in routes:
    route_code_by_id[r['route_id']] = int(r['route_short_name'])
  sequences = dict()
  for trip in trips:
    route_code = route_code_by_id[trip['route_id']]
    key = "%s-%s" % (route_code,trip['direction_id'])
    if key in sequences:
      n = sequences[key]+1
    else:
      n = 1
    trip['trip_id'] = "%s-%s" % (key,n)
    sequences[key] = n
  return trips

if __name__ == '__main__':
  datadir = sys.argv[1]
  routes = csvio.read('%s/routes.txt' % datadir)
  trips = csvio.read('%s/trips.txt' % datadir)
  trips = process(routes,trips)
  csvio.write('%s/trips.txt' % datadir,trips)
