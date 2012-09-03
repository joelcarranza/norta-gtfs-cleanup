import csvio
import sys
import re

# This cleans up stop names and tries to regularize them as much as possible

def normalize(value):
  return value.strip()

def process(stops):
  csvio.transform(stops,'stop_name',normalize)
  return stops

if __name__ == '__main__':
  datadir = sys.argv[1]
  stops = csvio.read('%s/stops.txt' % datadir)
  stops = process(stops)
  csvio.write('%s/stops.txt' % datadir,stops)
