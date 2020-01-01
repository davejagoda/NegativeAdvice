#!/usr/bin/env python3

from datetime import datetime
from datetime import timedelta
from datetime import timezone
from datetime import tzinfo

class UTC(tzinfo):
    '''UTC'''

    def utcoffset(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return 'UTC'

    def dst(self, dt):
        return timedelta(0)

def datetime_is_naive(dt):
    if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
        return('naive')
    else:
        return('aware')

if '__main__' == __name__:
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.now
    print('datetime.now() is {}'.format(datetime_is_naive(
        datetime.now())))
    print('datetime.now(UTC()) is {}'.format(datetime_is_naive(
        datetime.now(UTC()))))
    print('datetime.now(timezone.utc)) is {}'.format(datetime_is_naive(
        datetime.now(timezone.utc))))
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow
    print('datetime.utcnow() is {}'.format(datetime_is_naive(
        datetime.utcnow())))
    # https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp
    print('datetime.fromtimestamp(0) is {}'.format(datetime_is_naive(
        datetime.fromtimestamp(0))))
    print('datetime.fromtimestamp(0, UTC()) is {}'.format(datetime_is_naive(
        datetime.fromtimestamp(0, UTC()))))
    print('datetime.fromtimestamp(0, timezone.utc) is {}'.format(datetime_is_naive(
        datetime.fromtimestamp(0, timezone.utc))))
