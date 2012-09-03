import csvio
import sys

# This script aments GTFS feed with trip_bikes_allowed field
# as per: 
# https://groups.google.com/forum/?fromgroups#!topic/gtfs-changes/rEiSeKNc4cs

def process(routes,trips):
  route_type_by_id = {}
  for r in routes:
    route_type_by_id[r['route_id']] = int(r['route_type'])

  for trip in trips:
    route_id = trip['route_id']
    # 0 - Tram/Streetcar  3-bus
    route_type = route_type_by_id[route_id]
    # 2: bikes allowed on this trip 
    # 1: no bikes allowed on this trip 
    # 0: no information (same as field omitted) 
    if route_type == 3:
      trip['trip_bikes_allowed'] = 2
    elif route_type == 0:
      trip['trip_bikes_allowed'] = 1
    else:
      trip['trip_bikes_allowed'] = 0
  return trips

if __name__ == '__main__':
  datadir = sys.argv[1]
  routes = csvio.read('%s/routes.txt' % datadir)
  trips = csvio.read('%s/trips.txt' % datadir)
  trips = process(routes,trips)
  csvio.write('%s/trips.txt' % datadir,trips)
