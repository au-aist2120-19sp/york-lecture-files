# sometimes we CAN anticipate error conditions

x = int(input('enter a number: '))
if x == 0:
    print('BAD USER!!')
else:
    y = 10 / x

# sometimes we CAN anticipate error conditions
# BUT IT'S FRAKKING HARD

xstr = input('enter a number: ')
if xstr.isnumeric():
    x = int(xstr)
    if x == 0:
        print('BAD USER!!')
    else:
        y = 10 / x
else:
    print('BAD USER!!!')


# BUT, exception handling can be easier (and 
# perhaps safer)

try:
    x = int(input('enter a number: '))
    y = 10 / x
    print('the answer is ' + str(y))
except:
    print('BAD USER!!!')


# CAN have different except blocks
# BASED on the type of error / exception

try:
    x = int(input('enter a number: '))
    y = 10 / x
    print('the answer is ' + str(y))
except ZeroDivisionError:
    print('DUDE, YOU CAN\'T DIVIDE BY ZERO!!!')
except ValueError:
    print('DUDE, YOU ARE AN IDIOT. I SAID A NUMBER!!')


# Can capture the exception...

# CAN have different except blocks
# BASED on the type of error / exception

try:
    x = int(input('enter a number: '))
    y = 10 / x
    print('the answer is ' + str(y))
except ZeroDivisionError as ex:
    print('DUDE, YOU CAN\'T DIVIDE BY ZERO!!!')
    print(ex)
# except ValueError as ex:
#     print('DUDE, YOU ARE AN IDIOT. I SAID A NUMBER!!')
#     print(ex)
except Exception as ex:
    print("I DUNNO, SOMTHIN' HAPPENED")
    print(ex)




fn = input('Enter filename: ')
fi = open(fn,'r')
for line in fi:
    words = line.split()
    for word in words:
        print(word)

try:
    fn = input('Enter filename: ')
    with open(fn,'r') as fi:
        for line in fi:
            words = line.split()
            for word in words:
                print(word)
except:
    print('BADNESS!!!')

# Within a try
#    - except (IF AN EXCEPTION IS CAUGHT)
#    - finally (RUN CODE NO MATTER WHAT)
#    - else (RUN CODE ONLY IF SUCCESSFUL RUN WITHOUT EXCEPTION)
