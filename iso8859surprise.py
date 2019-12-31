#!/usr/bin/env python3

for i in range(256):
    s = chr(i)
    if (s.encode('utf8') != s.encode('iso-8859-1')):
        print('{} {} {} {}'.format(
            i, s, s.encode('utf8'), s.encode('iso-8859-1')))
