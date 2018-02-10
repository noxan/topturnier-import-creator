import os
import re
from Couple import Couple

def slugify(text):
    return re.sub(r'\W+', '-', text).lower()


def buildFilepath(league, dance):
    cwd = os.getcwd()
    filename = '{league}-{dance}.csv'.format(**{
        'league': slugify(league),
        'dance': slugify(dance),
    })
    return os.path.join(cwd, filename)


template = '{number};\
{surnameG};{lastnameG};\
{surnameL};{lastnameL};\
{institution}\n'


def writeExport(league, dance, couples):
    filepath = buildFilepath(league, dance)
    fh = open(filepath, 'w', encoding='cp1252')

    for couple in couples:
        # Number;HeFirstname;HeLastname;SheFirstname;SheLastname;Club
        if couple.participateClass(league, dance):
            fh.write(couple.printCoupleForTTList())

    fh.flush()
    fh.close()


#writeExport('Bronze', 'Langsamer Walzer', [{
#    'number': 1,
#    'surnameG': 'Super',
#    'lastnameG': 'Man',
#    'surnameL': 'Wonder',
#    'lastnameL': 'Woman',
#    'institution': 'World',
#}])
