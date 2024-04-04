
try:
    dong = '암사동'

    files = open('zipcode.txt')

    line = files.readline()
    while line:
        lines = line.split('\t')

        #print(len(lines))

        if lines[3].startswith(dong):
            print(lines)

        line = files.readline()
    files.close()
except Exception as e:
    print(e)
