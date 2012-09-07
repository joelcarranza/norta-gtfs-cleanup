import csv
from itertools import izip

# working with CSV files

def recode(dataset,column,trans):
  for row in dataset:
    if column in row:
      old_value = row[column]
      new_value = trans[old_value]
      row[column] = new_value

def transform(dataset,column,func):
  for row in dataset:
    if column in row:
      row[column] = func(row[column])

def read(filename):
  results = []
  header = None
  with open(filename, 'rb') as f:
      reader = csv.reader(f)
      for row in reader:
        if not header:
          header = row
        else:
          results.append(dict(izip(header,row)))
  return results

def write(filename,data,header=None):
  if not header:
    header = data[0].keys()
  with open(filename, 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for row in data:
      rowdata = [row.get(key,'') for key in header]
      writer.writerow(rowdata)
