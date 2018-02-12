import csv
from export import writeExport
from Couple import Couple

def getLastnameG(couple):
  return couple.lastnameG

def exportDance(dance, couples):
  writeExport("Goldstar", dance, couples)
  writeExport("Gold", dance, couples)
  writeExport("Silber", dance, couples)
  writeExport("Bronze", dance, couples)

with open('anmeldung.csv', 'r', encoding="UTF-8") as infile, open('anmeldungClean.csv', 'w') as outfile:
  data = infile.read()
  data = data.replace("&amp;", "&")
  outfile.write(data)

coupleNumber = 1
couples = []

with open('anmeldungClean.csv', newline='') as csvfile:

  spamreader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
  for row in spamreader:
    if(type(row['Startklasse Tanzschulturnier']) != str or type(row['Zuname Herr']) != str or type(row['Zuname Dame']) != str ):
      continue # simple filter for broken data sets
    if (not bool(row['Zuname Herr'])):
      continue
    coupleTemp = Couple(row)
    coupleTemp.number = coupleNumber

    print(str(coupleNumber) + " " + coupleTemp.surnameG)
    couples.append(coupleTemp)
  couples.sort(key=getLastnameG, reverse=False)
  for couple in couples:
    couple.number = coupleNumber
    coupleNumber += 1

with open('interimList.csv', 'w', newline='', encoding='utf-8') as csvfile:
  spamwriter = csv.writer(csvfile, delimiter=';',
                          quotechar='|', quoting=csv.QUOTE_MINIMAL)
  spamwriter.writerow(["Number" , "SurnameG", "LastnameG", "SurnameL", "LastnameL", "Institution", "DanceClass", "Starts"])
  for singleCouple in couples:
    spamwriter.writerow([ singleCouple.number,
                        singleCouple.surnameG, singleCouple.lastnameG,
                        singleCouple.surnameL, singleCouple.lastnameL,
                        singleCouple.institution,
                        singleCouple.danceClass, singleCouple.printStarts() ] )

exportDance("Langsamer Walzer", couples)
exportDance("Wiener Walzer", couples)
exportDance("Slow Fox", couples)
exportDance("Tango", couples)
exportDance("Quickstep", couples)
exportDance("Cha Cha Cha", couples)
exportDance("Rumba", couples)
exportDance("Samba", couples)
exportDance("Jive", couples)
exportDance("Paso Doble", couples)
exportDance("Salsa", couples)
exportDance("Discofox", couples)
