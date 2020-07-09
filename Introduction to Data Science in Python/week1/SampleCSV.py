import csv
def sample_csv():
  with open('sample.csv') as csvfile:
    sample = list(csv.DictReader(csvfile))
  print(sample)
  print(sample[:2]) # The first three dictionaries in our list.
  print(len(sample))
  print(sample[0].keys())
  print("Avg Age:: " + str(sum(int(d['Age'])for d in sample)/len(sample)))
  cities = set(d['City'] for d in sample)
  print(cities)

sample_csv()