import csvio
import sys
import re

# This cleans up stop names and tries to regularize them as much as possible

def normalize(name):
  name = name.strip()
  # remove duplicate spaces
  name = re.sub(r'\s+',' ',name)
  # Some stops end with strange stuff in parens
  # Ex: (In),(Out),(Nearside),(Farside) 
  # just remove
  name = re.sub(r'\(\w+\)$','',name)
  return name

def process(stops):
  csvio.transform(stops,'stop_name',normalize)
  return stops

if __name__ == '__main__':
  datadir = sys.argv[1]
  stops = csvio.read('%s/stops.txt' % datadir)
  stops = process(stops)
  csvio.write('%s/stops.txt' % datadir,stops)
