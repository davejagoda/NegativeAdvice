#!/usr/bin/python

# http://stackoverflow.com/questions/132988/is-there-a-difference-between-and-is-in-python

def izzit(start, step):
    i = j = start
    while i is j:
        was = i
        i += step
        j += step
    return(was, i)

print("counting down")
print("%i is\n%i is not" % izzit(0, -1))
print("counting up")
print("%i is\n%i is not" % izzit(0, 1))
