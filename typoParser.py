import csv
from Couple import Couple

def getLastnameG(couple):
  return couple.lastnameG

with open('anmeldung.csv', 'r', encoding="UTF-8") as infile, open('anmeldungClean.csv', 'w') as outfile:
  data = infile.read()
  data = data.replace("&amp;", "&")
  outfile.write(data)

coupleNumber = 1
couples = []

with open('anmeldungClean.csv', newline='') as csvfile:

  spamreader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
  for row in spamreader:
    if(type(row['Startklasse Tanzschulturnier']) != str or type(row['Zuname Herr']) != str):
      continue # simple filter for broken data sets
    coupleTemp = Couple(row)
    coupleTemp.number = coupleNumber
    
    print(str(coupleNumber) + " " + coupleTemp.surnameG)
    couples.append(coupleTemp)
    coupleNumber += 1
  couples.sort(key=getLastnameG, reverse=False)

with open('interimList.csv', 'w', newline='') as csvfile:
  spamwriter = csv.writer(csvfile, delimiter=';',
                          quotechar='|', quoting=csv.QUOTE_MINIMAL)
  spamwriter.writerow(["Number" , "SurnameG", "LastnameG", "SurnameL", "LastnameL", "Institution", "DanceClass", "Starts"])
  for singleCouple in couples:
    spamwriter.writerow([ singleCouple.number, 
                        singleCouple.surnameG, singleCouple.lastnameG, 
                        singleCouple.surnameL, singleCouple.lastnameL,
                        singleCouple.institution,
                        singleCouple.danceClass, singleCouple.printStarts() ] )

