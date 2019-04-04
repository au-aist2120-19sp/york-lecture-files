import os
import sys
import openpyxl as xl
from pprint import pprint as pp

# FUNCTIONS #

def check_exists(filename):
    if not os.path.exists(filename):
        print(f'ERROR: {filename} does not exist')
        exit()


# python gradeit.py [newgrades] [gradesheet] [translation]
# pp(sys.argv)

if len(sys.argv) != 4:
    print('USAGE: python gradeit.py [newgrades] [gradesheet] [translation]')
    exit()

newgrades = sys.argv[1]
gradesheet = sys.argv[2]
translation = sys.argv[3]

check_exists(newgrades)
check_exists(gradesheet)
check_exists(translation)

# open the newgrades file
# for every new grade
#    find the translation (i.e., email address) for the id
#    update the gradesheet for the student

ng_book = xl.load_workbook(newgrades)
#ng_sheet = ng_book.active
ng_sheet = ng_book.worksheets[0]

#for ng_row in ng_sheet.rows:
for ng_row in ng_sheet.iter_rows(2):
    #print(ng_row)
    id = ng_row[0].value
    grade = ng_row[1].value
    print(id, grade)

    # FIND associated email
    tr_book = xl.load_workbook(translation)
    tr_sheet = tr_book.worksheets[0]
    email = 'NA'
    for tr_row in tr_sheet.iter_rows(2):
        if tr_row[1].value == id:
            email = tr_row[0].value
            break
    print(f'{id}==>{email}')
    if email == 'NA':
        print(f"WARNING: {id} not found!")
        continue

    #assn = 'HW4'
    #print(newgrades)
    #..\..\HW4.xlsx
    pt_a = newgrades.split(os.sep)
    #["..", "..", "HW4.xlsx"]
    fn = pt_a[-1]
    #"HW4.xlsx"
    pt_b = fn.split('.')
    #["HW4", "xlsx"] 
    assn = pt_b[0]
    #"HW4"

    print(f"Now processing grade for {assn}")

    # STOPPING UNTIL THURSDAY

    tr_book.close()



ng_book.close()
