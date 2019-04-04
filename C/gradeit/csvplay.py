import csv
from pprint import pprint as pp

filename = '..\\..\\grades.csv'
with open(filename, 'rt') as fi:
    # lines = fi.readlines()
    # for line in lines:
    #     parts = line.split(',')
    #     print(parts)
    csr = csv.reader(fi)
    # for line in csr:
    #     print(line)
    cslist = list(csr)
    pp(cslist)
    print(cslist[2][1])
    