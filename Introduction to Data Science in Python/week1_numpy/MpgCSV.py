import csv


def mpg_csv():
  with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))
  print(mpg)
  print(mpg[:2]) # The first three dictionaries in our list.
  print(len(mpg))
  print(mpg[0].keys())
  print("City Millage:: " + str(sum(float(d['cty']) for d in mpg) / len(mpg)))
  print("Highway Millage:: " + str(sum(float(d['hwy']) for d in mpg) / len(mpg)))
  cylinders = set(d['cyl'] for d in mpg)
  cylinders
  print(cylinders)

  CtyMpgByCyl = []
  for c in cylinders: # iterate over all the cylinder levels
    summpg = 0
    cyltypecount = 0
    for d in mpg: # iterate over all dictionaries
      if d['cyl'] == c: # if the cylinder level type matches,
        summpg += float(d['cty']) # add the cty mpg
        cyltypecount += 1 # increment the count
    CtyMpgByCyl.append((c, summpg / cyltypecount)) # append the tuple ('cylinder', 'avg mpg')
  CtyMpgByCyl.sort(key=lambda x: x[0])
  print(CtyMpgByCyl)

  vehicleclass = set(d['class'] for d in mpg) # what are the class types
  print(vehicleclass)

  HwyMpgByClass = []

  for t in vehicleclass: # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg: # iterate over all dictionaries
      if d['class'] == t: # if the cylinder amount type matches,
        summpg += float(d['hwy']) # add the hwy mpg
        vclasscount += 1 # increment the count
    HwyMpgByClass.append((t, summpg / vclasscount)) # append the tuple ('class', 'avg mpg')

  HwyMpgByClass.sort(key=lambda x: x[1])
  print(HwyMpgByClass)

mpg_csv()

