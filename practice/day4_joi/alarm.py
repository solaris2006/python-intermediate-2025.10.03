#!/usr/bin/env python

"""
alarm-ing
"""

import sys
import datetime as dt
from time import sleep
from os import path
from subprocess import run


def parse_timespec(timespec):
    """
    parses a string of the form "HH" / "HH:MM" / "HH:MM:SS"
    and returns a `datetime.time` object
    """

    parts = timespec.split(':')

    if not (1 <= len(parts) <= 3):
        raise ValueError("`timespec` must be of the form HH / HH:MM / HH:MM:SS")
    
    # we construct a time object from the given timespec parts.
    # (we must convert each of them to int.)
    return dt.time(*map(int, parts))


def seconds_to_ts(time):
    """
    given a `datetime.time` object, returns
    the number of seconds from now to that moment.

    it works even if the timestamp occurs on the next day.
    """
    today = dt.date.today()
    future = dt.datetime.combine(today, time) # datetime.datetime

    now = dt.datetime.now()

    if future < now:
        # the given time will occur tomorrow
        future += dt.timedelta(days=1)

    delta = future - now
    return delta.total_seconds()


def schedule(wait, payload):
    "schedules `payload` to be called after `wait` seconds."

    # 1. wait
    print(f"waiting for {wait} seconds")
    sleep(wait)

    # 2. execute
    payload()


def mknotification(time):
    def notify():
        message = f"Este ora {time}!"
        run([
            'notify-send',
             '-a', "Alarm",
              message
        ])

    return notify


if __name__ == "__main__":
    # I am a script

    try:
        timespec = sys.argv[1]

    except IndexError:
        scriptname = path.basename(sys.argv[0])
        print(f"Usage: {scriptname} <timespec>", file=sys.stderr)
        sys.exit(1)

    time = parse_timespec(timespec)
    wait = seconds_to_ts(time)

    payload = mknotification(time)

    schedule(wait, payload)
