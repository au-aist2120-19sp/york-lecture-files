
# strn = 'Hey give me a buzz at 706-555-1212.'

# words = strn.split()
# for word in words:
#     first = word[0]
#     if not first.isdigit():
#         continue
#     word = word.replace('.', '')
#     word = word.replace(',', '')
#     word = word.replace('!', '')
#     word = word.replace('?', '')
#     parts = word.split('-')
#     if len(parts) != 3:
#         continue
#     try:
#         num1 = int(parts[0])
#         if num1 < 200 or num1 > 999:
#             continue
#         num2 = int(parts[1])
#         if num2 < 200 or num2 > 999:
#             continue
#         num3 = int(parts[2])
#         if len(parts[2]) != 4:
#             continue
#     except:
#         continue

#     print(word)

import re

strn = 'Hey give me a buzz at 706-555-1212.'

print("PART 1")
regex1 = re.compile('give')
match = regex1.search(strn)
if match:  # TRUTHY
    #print(match)
    print(match.group())
else:
    print("NO MATCH")

print("PART 2")
regex2 = re.compile('gave')
match = regex2.search(strn)
if match:  # TRUTHY
    print(match.group())
else:
    print("NO MATCH")

print("PART 3")
regex3 = re.compile(r'g[ai]ve\w*')
match = regex3.search(strn)
if match:  # TRUTHY
    print(match.group())
else:
    print("NO MATCH")

strn2 = 'The rain in Spain falls mainly on the plain.'

print("PART 4")
regex4 = re.compile(r'ain')
matches = regex4.findall(strn2)
if matches:  # TRUTHY
    for match in matches:
        print(match)
else:
    print("NO MATCH")

# CHARACTER CLASSES
# \d    DIGIT (0-9)
# \D    NOT A DIGIT
# \w    TEXT (letter, digit, or _)
# \W    NOT TEXT
# \s    Whitespace (space, newline, tab, etc.)
# \S    NOT Whitespace

print("PART 5")
regex5 = re.compile(r'\wain')
matches = regex5.findall(strn2)
if matches:  # TRUTHY
    for match in matches:
        print(match)
else:
    print("NO MATCH")

# QUANTITY MODIFIERS
# ?     Match zero or one (OPTIONAL)   '(re)?match'
# *     Match zero to many
# +     Match one or more '(great-)+grandchildren'
# {m}   Match EXACTLY m '(great-){2}grandchildren'
# {m,n} Match between m and n
# {,n}  Match at most n
# {m,}  Match at least m

print("PART 6")
regex6 = re.compile(r'\w*ain\w*')
matches = regex6.findall(strn2)
if matches:  # TRUTHY
    for match in matches:
        print(match)
else:
    print("NO MATCH")

print("PART 7")
regex7 = re.compile(r'\w*ain')
newstrn = regex7.sub('POOP', strn2)
print(newstrn)

# regex for a phone

strn3 = '''
Hey give me a buzz at 706-555-1212.
Or maybe at 404 555 1212.
Or perhaps 912.555.1212.
Or even 6785551212.
But NOT 123-123-1234.
'''

print("PART 8")
regex8 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matches = regex8.findall(strn3)
if matches:  # TRUTHY
    for match in matches:
        print(match)
else:
    print("NO MATCH")

# CUSTOM CHARACTER CLASSES
# [...]
# [aeiou]       - lowercase vowels
# [aeiouAEIOU]  - all vowels
# [23456789]    - only 2-9
# [2-9]         - same same
# [0-9A-Fa-f]   - Hexadecimal digit (r'#[0-9A-Fa-f]{6}')

print("PART 9")
regex9 = re.compile(r'[2-9]\d\d[- .]?[2-9]\d\d[- .]?\d\d\d\d')
matches = regex9.findall(strn3)
if matches:  # TRUTHY
    for match in matches:
        print(match)
else:
    print("NO MATCH")

# ^...  Match ONLY if it is at the beginning
# ...$  Match ONLY if it is at the end

para = '''
Hey my name is Paul. My email address is paul.york@augusta.edu.
I live in Augusta.  And, I teach at AU.'''

print("PART 10")
para = para.strip()
regex10 = re.compile(r'\.\s+|\.$')
sents = regex10.split(para)
print(sents)

print("PART 11")
regex11 = re.compile(r'\.\s+|\.$|,\s+|\s')
words = regex11.split(para)
print(words)

exit(100)

