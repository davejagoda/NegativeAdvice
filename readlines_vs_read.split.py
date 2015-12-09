#!/usr/bin/python

import sys

if '__main__' == __name__:
    for arg in sys.argv:
        print('processing file: {}'.format(arg))
        with open(arg, 'r') as f:
            print('f.readlines() found {} lines'.format(len(f.readlines())))
        with open(arg, 'r') as f:
            print('f.read().split() found {} lines'.format(len(f.read().split('\n'))))
        print
