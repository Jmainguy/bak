#!/usr/bin/python

import sys
import argparse
import shutil
import time
import os

parser = argparse.ArgumentParser(description='Backup a file, defaults to same path and .bak. \
                                              overwrites backup if exists')

parser.add_argument('-a', '--append', help='characters to append to source file instead of .bak', type=str)
parser.add_argument('-d', '--date', action='store_true', help='add the date .YYYYMMDD to the end of the file')
parser.add_argument('-f', '--force', action='store_true', help='overwrite backup if exists')
parser.add_argument('Source', help='file to backup')
args = parser.parse_args()
duplicate = int(1)

def checkdest(dest, duplicate):
    if os.path.exists(dest):
        if os.path.exists("%s(%s)" % (dest, duplicate)):
            duplicate += 1
            dest = checkdest(dest, duplicate)
        else:
            dest = "%s(%s)" % (dest, duplicate)
    return dest

def main(args):
    append = args.append
    date = args.date
    source = args.Source
    force = args.force
    arglist = list()

    if source[-1] == '/':
        source = source[:-1]

    arglist.append(source)

    if not append:
        append = 'bak'

    arglist.append(append)

    if date:
        date = time.strftime('%Y%m%d')
        arglist.append(date)
    
    dest = '.'.join(arglist)

    if not force:
        dest = checkdest(dest, duplicate)

    if os.path.isfile(source):
        shutil.copy(source, dest)
    elif os.path.isdir(source):
        if os.path.isdir(dest):
            shutil.rmtree(dest)
        shutil.copytree(source, dest)
    else:
        print "%s does not exist" % source
        sys.exit(1)

main(args)
