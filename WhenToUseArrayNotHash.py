#!/usr/bin/python

hash = { 'first'   : 1,
         'second'  : 2,
         'third'   : 3,
         'fourth'  : 4,
         'fifth'   : 5,
         'sixth'   : 6,
         'seventh' : 7,
         'eighth'  : 8,
         'ninth'   : 9,
         'tenth'   : 10 }

print(hash)
print(sorted(hash.values()))
print(sorted(hash, key=hash.get))
