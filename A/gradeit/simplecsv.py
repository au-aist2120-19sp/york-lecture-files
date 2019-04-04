import csv

filename = "..\\..\\grades.csv"

with open(filename, 'rt') as fi:
    # l = fi.readlines()
    # for t in l:
    #     print(t)
    csvr = csv.reader(fi)
    csvl = list(csvr)
    cnt = 0
    print(csvl[1][0])
    for line in csvr:
        if cnt > 0:
            print(cnt, line[0])
        cnt += 1
