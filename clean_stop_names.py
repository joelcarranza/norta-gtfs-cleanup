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
r'\(\w+\)$',''
)

SPELLING = (
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
'Loyola/Tulane','Tulane/Loyola',
"D' Hemecourt","D'Hemecourt",
"F C Williams","Fannie C Williams",
"Saint Paul's Church","Saint Paul's",
"Majestic Oakss","Majestic Oaks"
)

REMAP = (
"Paris Ave at Aviator","Paris Ave at Aviators",
"Downman at Fillmore","Downman at Filmore",
"Monroe at Mark","Monroe at Marks",
"Woodlawn at Tall Timbers","Woodland at Tall Timbers",
# carrolton
"Canal and Carrollton","Canal and S Carrollton",
"Canal at Carrollton","Canal at S Carrollton",
"Carrollton at Canal","S Carrollton at Canal",
"Carrollton at S Claiborne","S Carrollton at S Claiborne",
"Carrollton at Willow","S Carrollton at Willow",
"Claiborne at Carrollton","S Claiborne at S Carrollton",
# claiborne
"Claiborne at Washington","S Claiborne at Washington",
"Esplanade at Claiborne","Esplanade at N Claiborne",
"M L King at Claiborne","M L King at S Claiborne",
"Napoleon at Claiborne","Napoleon at S Claiborne",
"Washington at Claiborne","Washington at S Claiborne",
# broad
"St Bernard at Broad","St Bernard at N Broad",
"Tulane at Broad","Tulane at S Broad",
"Washington at Broad","Washington at S Broad",
"Broad at Washington","S Broad at Washington"
# paris
"Paris at Burbank","Paris Ave at Burbank",
"Paris at Mirabeau","Paris Ave at Mirabeau",
"Mirabeau at Paris","Mirabeau at Paris Ave"
)

def normalize(name):
  name = name.strip()
  for i in xrange(0,len(RULES),2):
    name = re.sub(RULES[i],RULES[i+1],name)
  for i in xrange(0,len(SPELLING),2):
    name = re.sub(r'\b'+re.escape(SPELLING[i])+r'\b',SPELLING[i+1],name)
  for i in xrange(0,len(REMAP),2):
    if name == REMAP[i]:
      name = REMAP[i+1]
  return name

def process(stops):
  csvio.transform(stops,'stop_name',normalize)
  return stops

if __name__ == '__main__':
  datadir = sys.argv[1]
  stops = csvio.read('%s/stops.txt' % datadir)
  stops = process(stops)
  csvio.write('%s/stops.txt' % datadir,stops)
