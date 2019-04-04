from pprint import pprint as pp
import sys
import os
import openpyxl as xl

# FUNCTIONS #

def check_exists(filename):
    if not os.path.exists(filename):
        print(f"ERROR: {filename} doesn't exist")
        exit()

# python gradeit.py [newgrades] [gradesheet] [translation]

#pp(sys.argv)

if len(sys.argv) != 4:
    print('USAGE: python gradeit.py [newgrades] [gradesheet] [translation]')
    exit()

newgrades = sys.argv[1]
gradesheet = sys.argv[2]
translation = sys.argv[3]

#print(newgrades, gradesheet, translation)

check_exists(newgrades)
check_exists(gradesheet)
check_exists(translation)

'''
1) open newgrades
2) for each grade
    2a) read id and grade
    2b) find email associated with id (using translation)
    2c) using gradesheet find right col and row for assignment and email
    2d) write grade in correct cell
3) save gradesheet
'''

ng_book = xl.load_workbook(newgrades)
ng_sheet = ng_book.worksheets[0]

# Read grades from newgrades
#for row in ng_sheet.rows:
for row in ng_sheet.iter_rows(2):
    #pp(row)
    ghid = row[0].value
    grade = row[1].value
    print(ghid, grade)

    # FIND email for the id
    tr_book = xl.load_workbook(translation)
    tr_sheet = tr_book.worksheets[0]
    email = 'NA'
    for tr_row in tr_sheet.iter_rows(2):
        if ghid == tr_row[1].value:
            email = tr_row[0].value
            break

    if email == 'NA':
        print(f"WARNING: {ghid} not found")
        continue

    print(f"{ghid} actually is {email}")

    part_a = newgrades.split(os.sep) # ["..","..","HW4.xlsx"]
    fn = part_a[-1] # "HW4.xlsx"
    part_b = fn.split('.') # ["HW4", "xlsx"]
    assn = part_b[0]

    print(f'PROCESSING: {assn}')

    # DONE FOR TODAY

ng_book.close()