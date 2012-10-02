import csvio
import sys
import re

# This cleans up stop names and tries to regularize them as much as possible
RULES = (
# squeeze out any reference to space
# N.Canal -> N Canal
r'\.',' ',
# now normalize spaces 
r'\s+',' ',
# remmove trailing parantheticals
r'\(\w+\)$','',
# spelling errors
'Annunciation','Annunication',
'Behman','Behrman',
'Carondolet','Carondelet',
'Derbingy','Derbigny',
'Downmam','Downman',
'Dumanie','Dumaine',
'Elks Place','Elk Place',
'Esplanande','Esplanade',
'Esplande','Esplanade',
'Lonely Oaks','Lonely Oak',
'Majestic Oak','Majestic Oaks',
'Newcastle','New Castle',
'Opeloousas','Opelousas',
'Preiur','Prieur',
'Wiliams','Williams',
'First','1st',
'Loyola/Tulane','Tulane/Loyola'
)

def normalize(name):
  name = name.strip()
  for i in xrange(0,len(RULES),2):
    name = re.sub(RULES[i],RULES[i+1],name)
  return name

def process(stops):
  csvio.transform(stops,'stop_name',normalize)
  return stops

if __name__ == '__main__':
  datadir = sys.argv[1]
  stops = csvio.read('%s/stops.txt' % datadir)
  stops = process(stops)
  csvio.write('%s/stops.txt' % datadir,stops)
