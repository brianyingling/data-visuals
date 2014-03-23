import csv

MY_FILE = "./data/sample_sfpd_incident_all.csv"

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

def main():
  new_data = parse(MY_FILE,',')
  print new_data


if __name__ == "__main__":
  main()
