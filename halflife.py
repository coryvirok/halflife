"""
Prints out the date in the future when you will be twice as old as you were
on 1998-07-31.

Usage:
    python halflife.py BIRTH_YEAR BIRTH_MONTH BIRTH_DATE

"""

import datetime
import time
import sys


if __name__ == '__main__':
    """
    y = (mx + b) / 2
    y = nx + c

    (mx + b) / 2 = nx + c
    mx + b = 2nx + 2c
    mx - 2nx = 2c - b
    (m - 2n)x = 2c - b
    x = (2c - b) / (m - 2n)

    birth_ts = 1981-01-13
    half_life = (x + -birth_ts) / 2

    ccd_ts = 1998-07-31
    ccd = x + ccd_ts

    x = ((2 * -ccd_ts) + birth_ts) / (1 - 2)
    """

    birth_year, birth_month, birth_date = map(int, sys.argv[1:])

    birth = datetime.datetime(birth_year, birth_month, birth_date)
    ccd = datetime.datetime(1998, 7, 31)
    ccd_ts = time.mktime(ccd.timetuple())
    birth_ts = time.mktime(birth.timetuple())

    x = ((2 * -ccd_ts) + birth_ts) / (1 - 2)

    half = datetime.datetime.fromtimestamp(x)
    half_ts = x

    now = datetime.datetime.now()
    now_ts = time.mktime(now.timetuple())

    end = (now_ts, now, ccd_ts, ccd, now - ccd)
    tmp = (half_ts, half, ccd_ts, ccd, half - ccd)
    start = (ccd_ts, ccd, birth_ts, birth, ccd - birth)

    print half
    print

    print 'Checksum:'
    print 'now: %d (%s) - ccd: %d (%s) = %s' % end
    print 'half: %d (%s) - ccd: %d (%s) = %s' % tmp
    print 'ccd: %d (%s) - birth: %d (%s) = %s' % start

