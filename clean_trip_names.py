import csvio
import sys
import re

# This cleans up trip names and tries to regularize them as much as possible

def normalize(value):
  return value.strip()

def process(trips):
  csvio.transform(trips,'trip_headsign',normalize)
  return trips

if __name__ == '__main__':
  datadir = sys.argv[1]
  trips = csvio.read('%s/trips.txt' % datadir)
  trips = process(trips)
  csvio.write('%s/trips.txt' % datadir,trips)
