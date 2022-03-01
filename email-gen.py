#
# Created by MØSER D3 © 2021
#

import random

DOMAIN = '@company.io'
IN_FILE = 'task_file.txt'
OUT_FILE = 'task_file2.txt'
DIGITS = '1234567890'
U_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
L_CHARS = 'abcdefghijklmnopqrstuvwxyz' 
SYMBOLS = '!@#$%^&*()-+'
PWD_LEN = 12

def process_line(line):
    line = line.replace(' ','')
    # сдель нужно обработать линию, если линия не валидная - вернуть пустую строку
    return line

def genpwd():
    pwd = ''
    var = [DIGITS, U_CHARS, L_CHARS, SYMBOLS]
    pwd += random.choice(DIGITS)
    pwd += random.choice(U_CHARS)
    pwd += random.choice(L_CHARS)
    pwd += random.choice(SYMBOLS)
    while len(pwd) < PWD_LEN:
        pwd += random.choice(var[random.randint(0, len(var) - 1)])
    return pwd

def main():
    file = open(IN_FILE, 'r')
    lines = file.readlines()
    file.close()

    file = open(OUT_FILE, 'w')
    i = 1
    for line in lines:
        line = process_line(line)
        if len(line) < 1:
            continue
        name = line.split(',')
        out = '{0} - {1} {2}, email: {3}.{4}{5}/{6}'.format(\
            i, name[1], name[2], name[2].lower(), name[1].lower(), DOMAIN, genpwd())
        print(out)
        file.write('{0}\n'.format(out))
        i += 1

    file.close()
    return 0

if __name__ == '__main__':
    main()
