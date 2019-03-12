# prevent divide by 0 PROACTIVELY

num = input("give me a number: ")
if num.isdigit():
    n = int(num)
    if n != 0:
        inv = 1 / n
        print(f"the inverse of {n} is {inv}")
    else:
        print("Can't divide by 0")
else:
    print("I meant a REAL number")

# NEWFANGLED way of handing errors REACTIVELY

try:
    n = int(input("give me a number: "))
    print(f"the inverse of {n} is {1 / n}")
except:
    print("Oops. You screwed up.")


# BETTER exception handling

try:
    n = int(input("give me a number: "))
    print(f"the inverse of {n} is {1 / n}")
except ValueError:
    print("No I meant a REAL number")
except ZeroDivisionError:
    print("Can't divide by zero")


# other members of the exception handling fam

try:
    fn = input("Enter a file name: ")
    fi = open(fn, 'r')
    for line in fi:
        # A line contains name,averge
        parts = line.split(',')
        name = parts[0]
        average = float(parts[1])
        average += 1 / average
        print(f"{name} earned a {average}")
except ValueError:
    print("No I meant a REAL number")
except FileNotFoundError:
    print("Sorry dude, can't find that file")
except:
    print("Not sure what, but something bad happened")
else:
    print("RUNS IF NO EXCEPTION OCCURRED")
finally:
    # Catch anything and ignore it (USE WITH EXTREME CAUTION)
    try:
        fi.close()
    except:
        pass


# Moar better way of "catching" exceptions

try:
    fn = input("Enter a file name: ")
    fi = open(fn, 'r')
    for line in fi:
        # A line contains name,averge
        parts = line.split(',')
        name = parts[0]
        average = float(parts[1])
        average += 1 / average
        print(f"{name} earned a {average}")
except ValueError as ex:
    print("No I meant a REAL number")
    print(ex)
except FileNotFoundError as ex:
    print("Sorry dude, can't find that file")
    print(ex)
except Exception as ex:
    print("Not sure what, but something bad happened")
    print(ex)
else:
    print("RUNS IF NO EXCEPTION OCCURRED")
finally:
    # Catch anything and ignore it (USE WITH EXTREME CAUTION)
    try:
        fi.close()
    except:
        pass


