#!/usr/bin/python

def output(f, msg):
    if f.closed:
        status = 'closed'
    else:
        status = 'open'
    print('after ' + msg + ', file is:' + status)

f = open('/dev/null')
output(f, 'f.open')
f.close
output(f, 'f.close')
f.close()
output(f, 'f.close()')
