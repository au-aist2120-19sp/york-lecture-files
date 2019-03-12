try:
    fn = input('Enter filename: ')
    with open(fn,'r') as fi:
        for line in fi:
            words = line.split()
            for word in words:
                print(word)
except:
    print('BADNESS!!!')
