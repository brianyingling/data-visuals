from collections import Counter

import csv
import matplotlib.pyplot as plt 
import numpy.numarray    as na

MY_FILE = "../data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimiter):
  """Parses a raw CSV file to a JSON-like object"""

  opened_file = open(raw_file, 'rU')
  csv_data    = csv.reader(opened_file, delimiter=delimiter)

  parsed_data = []

  fields = csv_data.next()

  for row in csv_data:
    parsed_data.append(dict(zip(fields,row)))

  opened_file.close()

  return parsed_data

def visualize_type():
  """Visualize data by category in a bar graph"""
  
  data_file = parse(MY_FILE, ',')

  # num of incidents per category
  counter = Counter(item['Category'] for item in data_file)

  # Set the labels
  labels = tuple(counter.keys())

  # Set exactly where the labels hit the x-axis
  xlocations = na.array(range(len(labels))) + 0.5

  # Width of each bar
  width = 0.5

  # Assign data to a bar plot
  plt.bar(xlocations, counter.values(), width=width)

  # Assign labels and tick location to x-axis
  plt.xticks(xlocations + width / 2, labels, rotation=90)
  
  # Give some more room so the x-axis labels aren't cut off
  plt.subplots_adjust(bottom=0.4)

  # Make the overall graph/figure larger
  plt.rcParams['figure.figsize'] = 12, 8

  # save
  plt.savefig('Type.png')

  # close
  plt.clf()


def visualize_days():
  """Visualize data by day of week"""

  # grab our parsed data that we parsed earlier
  data_file = parse(MY_FILE, ",")

  counter = Counter(item['DayOfWeek'] for item in data_file)

  data_list = [
    counter['Monday'],
    counter['Tuesday'],
    counter['Wednesday'],
    counter['Thursday'],
    counter['Friday'],
    counter['Saturday'],
    counter['Sunday']
  ]

  day_tuple = tuple(['Mon','Tues','Wed','Thurs','Fri','Sat','Sun'])

  plt.plot(data_list)

  # num of ticks needed for our x-axis & assign labels
  plt.xticks(range(len(day_tuple)),day_tuple)
  
  plt.savefig("Days.png")
  plt.clf()



def main():
  # visualize_days()
  visualize_type()

if __name__ == "__main__":
  main()
