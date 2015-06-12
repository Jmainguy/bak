#!/usr/bin/python

import sys
import argparse
import shutil
import time

parser = argparse.ArgumentParser(description='Backup a file, defaults to same path and .bak')

parser.add_argument('-a', '--append', help='characters to append to source file instead of .bak', type=str)
parser.add_argument('-d', '--date', action='store_true', help='add the date .YYYYMMDD to the end of the file')
parser.add_argument('source', help='file to backup')
args = parser.parse_args()

def main(args):
    append = args.append
    date = args.date
    source = args.source
    arglist = list()
    arglist.append(source)

    if not append:
        append = 'bak'
    arglist.append(append)
    if date:
        date = time.strftime('%Y%m%d')
        arglist.append(date)
    
    dest = '.'.join(arglist)
    shutil.copy(source, dest)

main(args)
