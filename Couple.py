class Couple:
  surnameG = ""
  lastnameG = ""
  surnameL = ""
  lastnameL = ""
  institution = ""
  number = -1
  danceClass = ""
  starts = []

  def appendStarts(self, dance, field):
    if(field.find('ja')>=0):
      self.starts.append(dance)


  def __init__(self, row):
    self.surnameG = row['Vorname Herr']
    self.lastnameG = row['Zuname Herr']
    self.surnameL = row['Vorname Dame']
    self.lastnameL = row['Zuname Herr']
    self.danceClass = row['Startklasse Tanzschulturnier']
    self.institution = row['Heimatverein/Tanzschule']
    self.appendStarts("Langsamer Walzer",row['Langsamer Walzer'])
    self.appendStarts("Wiener Walzer",row['Wiener Walzer'])
    self.appendStarts("Tango",row['Tango'])
    self.appendStarts("Quickstep",row['Quickstep'])
    self.appendStarts("Slow Fox",row['Slow Fox'])
    self.appendStarts("Cha Cha Cha",row['Cha Cha Cha'])
    self.appendStarts("Samba",row['Samba'])
    self.appendStarts("Rumba",row['Rumba'])
    self.appendStarts("Paso Doble",row['Paso Doble'])
    self.appendStarts("Jive",row['Jive'])
    self.appendStarts("Salsa",row['Salsa'])
    self.appendStarts("Discofox",row['Discofox'])
    
  def printStarts(self):
    printStart = ""
    for start in self.starts:
      printStart += (" , " + start)
    return printStart

