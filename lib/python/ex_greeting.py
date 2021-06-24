#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import datetime

import pytz
import tzlocal

def main():
    """
    Example code skeleton: Just greeting
    """
    argpsr = argparse.ArgumentParser(description='Example: showing greeting words')
    argpsr.add_argument('name', nargs='*', type=str, default=['World'],  help='your name') 
    argpsr.add_argument('-d', '--date', action='store_true', help='Show current date & time') 
    args = argpsr.parse_args()
    if args.date:
        tz_local = tzlocal.get_localzone()
        datestr  = datetime.datetime.now(tz=tz_local).strftime(" It is \"%c.\"")
    else:
        datestr = ''
    print ("Hello, %s!%s" % (' '.join(args.name), datestr))

if __name__ == '__main__':
    main()
