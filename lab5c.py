#!/usr/bin/env python3
# Author ID: Sadebola

def add(number1, number2):
    try:
        # Try converting to int and adding
        return int(number1) + int(number2)
    except (ValueError, TypeError):
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError):
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10,5))                        # should print 15
    print(add('10',5))                      # should print 15
    print(add('abc',5))                     # should print error message
    print(read_file('seneca2.txt'))         # should print file lines if file exists
    print(read_file('file10000.txt'))       # should print error message
