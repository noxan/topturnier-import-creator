import os
import re


def slugify(text):
    return re.sub(r'\W+', '-', text).lower()


def buildFilepath(league, dance):
    cwd = os.getcwd()
    filename = '{league}-{dance}.csv'.format(**{
        'league': slugify(league),
        'dance': slugify(dance),
    })
    return os.path.join(cwd, filename)


def writeExport(league, dance, couples):
    filepath = buildFilepath(league, dance)
    fh = open(filepath, 'w', encoding='cp1252')

    fh.write('World')

    fh.flush()
    fh.close()


writeExport('Bronze', 'Langsamer Walzer', [])
