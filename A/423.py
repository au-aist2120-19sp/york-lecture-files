def isphone(test):
    parts = test.split('-')  # ['###','###','####']
    if len(parts) != 3:
        return False
    if len(parts[0]) != 3:
        return False
    if len(parts[1]) != 3:
        return False
    if len(parts[2]) != 4:
        return False
    try:
        pt1 = int(parts[0])
        pt2 = int(parts[1])
        _ = int(parts[2])
        if pt1 < 100:
            return False
        if pt2 < 100:
            return False
    except:
        return False
    return True



# REGULAR EXPRESSIONS ROCK!!

import re

strn = 'Hey, give me a call. My digits are 706-555-1212.'

# strn = strn.replace('.','')
# strn = strn.replace(',','')
# words = strn.split()
# for word in words:
#     if isphone(word):
#         print(word)


re1 = re.compile('g[i|a]ve')

print('PART 1')
found = re1.search(strn)
if found:   # Truthy 
    print(found.group())
else:
    print('IT AIN\'T IN THERE')

print('PART 2')
findings = re1.findall(strn)
for finding in findings:
    print(finding)

print('PART 3')
newstrn = re1.sub('BLEEP', strn)
print(newstrn)

# CHARACTER CLASSES
# \d    DIGIT (0-9)
# \D    NOT DIGIT
# \w    Digit, character or underscore
# \W    NOT the above
# \s    Whitespace (space, newline, tab, etc.)
# \S    NOT whitespace
# .     ANY THING

# CUSTOM:
#  [aeiou]  Vowel class
#  [A-F]    All capital letters from A to F
#  [2-9]    All digits from 2 to 9
#  [23456789] Same as above
#  [2|9]    All digits that are either 2|9

print('PART 4')
re2 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match = re2.search(strn)
if match:
    print(match.group())

print('PART 5')
re3 = re.compile(r'[2-9]\d\d-[2-9]\d\d-\d\d\d\d')
match = re3.search(strn)
if match:
    print(match.group())


strn = '''
Hey, give me a call. My digits are 706-555-1212.
If I don't answer, call my mommy at 123-123-4567.
Or my daddy at 678 555 1212.
Or my granny at 770-5551212.
'''

print('PART 6')
# re3 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
re3 = re.compile(r'[2-9]\d\d-[2-9]\d\d-\d\d\d\d')
matches = re3.findall(strn)
if matches:
    for match in matches:
        print(match)
else:
    print("NO MATCH")


# SPECIAL CHARACTERS QUANTITY OF MATCHES
# ? MATCH ZERO OR ONE
# * MATCH ZERO OR MANY
# + MATCH ONE OR MANY
# {3,5} BETWEEN 3 and 5
# {m,n} BETWEEN m and n
# {,n} AT MOST n
# {m,} AT LEAST m
# {m} EXACTLY m

print('PART 7')
re3 = re.compile(r'[2-9]\d\d[- ]?[2-9]\d\d[- ]?\d\d\d\d')
matches = re3.findall(strn)
if matches:
    for match in matches:
        print(match)
else:
    print("NO MATCH")

print('PART 8')
re3 = re.compile(r'[2-9]\d{2}[- ]?[2-9]\d{2}[- ]?\d{4}')
matches = re3.findall(strn)
if matches:
    for match in matches:
        print(match)
else:
    print("NO MATCH")

print('PART 9')
re3 = re.compile(r'.*')
matches = re3.findall(strn)
if matches:
    for match in matches:
        print(match)
else:
    print("NO MATCH")

# ^...   Caret means start at the beginning
# ...$   Match from the end

phrase = 'Hello world. My name is paul.york.  I\'m really awesome.'

splitter = re.compile(r'\.\s+|\.$')
sents = splitter.split(phrase)
print(sents)

splitter2 = re.compile(r'\.\s+|\.$|\s+')
words = splitter2.split(phrase)
print(words)
