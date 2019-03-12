try:
    fn = input('Enter filename: ')
    fi = open(fn,'r')
    for line in fi:
        words = line.split()
        for word in words:
            print(word)
except FileNotFoundError:
    print('not found!!!')
finally:
    # if 'fi' in dir():
    #     print('CLOSING')
    #     fi.close()
    try:
        fi.close()
    except: pass
