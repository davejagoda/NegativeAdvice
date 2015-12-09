#!/usr/bin/python

# see this: http://www.peterbe.com/plog/blogitem-040312-1
# this comment explains the gotcha that I've coded below
# minhducit 09 June 2008
# In your code f.read().split('\n') will return one more line comparing with the f.readlines().
# However the last line is ""
# So they are not equal :)

import sys

if '__main__' == __name__:
    for arg in sys.argv:
        print('processing file: {}'.format(arg))
        with open(arg, 'r') as f:
            print('f.readlines() found {} lines'.format(len(f.readlines())))
        with open(arg, 'r') as f:
            print('f.read().split() found {} lines'.format(len(f.read().split('\n'))))
        print
