#!/usr/bin/env python3
import subprocess
from multiprocessing import Pool
from functools import partial
import os
import argparse

parser = argparse.ArgumentParser(description=
                                 "Description: Directory copy with rsync using multiprocessing. \n"
                                 "\nBY DEFAULT, the files will only be counted. \nUse optional parameters to list the files and/or perfom rsync copy"
                                 "\nDirectory will be copied to a new repository named <repo-name>-backup.\n"
                                 "\n           DEFAULT directory is my-sec-repo\n",
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 add_help=True)
# parser.add_argument(dest='sourceloc', type=str,
#                     help='Source folder  to be copied')
#
# parser.add_argument(dest='backuploc', type=str,
#                     help='Destination location of copied folder')

parser.add_argument('-p', '--processors', dest='processors', type=int,
                    help='The number of processors used.  Default=1')

parser.add_argument('-o', '--override', dest='override_repo', type=str,
                    help='Overrides the default source repository with provided repo')

parser.add_argument('-v', '--verbose', action='store_true',
                    help='Prints the list of files to be copied to the screen')

parser.add_argument('-s', '--syncargs', dest='syncargs', type=str, default="arq",
                    help='Parameters used for rsynch execution.  Provide a string WITHOUT SPACES OR LEADING DASH. e.g. arq'
                         'See rsync help for details')

parser.add_argument('--runsync', dest='runsync', action='store_true',
                    help='Perform the actual rsync operation')

args = parser.parse_args()

_syncargs = '-arq'
_sourceloc = 'my-sec-repo'

if args.override_repo != None:
    _sourceloc = args.override_repo
    print("Override initiated. Source repo is {}".format(_sourceloc))

if args.syncargs != None:
    _syncargs = "-" + args.syncargs
    print("Rsync arguments provided: {}".format(args.syncargs))

_sourcedir = '/home/adouglasx/repos/' + _sourceloc + '/'
_backupdir = '/home/adouglasx/repos/' + _sourceloc + '-backup/'

print("Source: {}".format(_sourcedir))
print("Destination: {}".format(_backupdir))
print("Rsync args: {}".format(_syncargs))


def run_sync(src, sourcedir, backupdir, syncargs):
    dest = src.replace(sourcedir, backupdir)
    if args.verbose:
        print(src)
    if args.runsync:
        subprocess.call(["rsync", syncargs, src, dest])


def create_file_lists(sourcedir):
    sourcelist = []
    for root, dirs, files in os.walk(sourcedir):
        for name in files:
            sourcefile = (os.path.join(root, name))
            sourcelist.append(sourcefile)
        for name in dirs:
            # sourcelist.append(os.path.join(root, name))
            pass
    return sourcelist


if __name__ == '__main__':

    if os.path.exists(_sourcedir):
        sourcelist = create_file_lists(_sourcedir)
        if len(sourcelist) > 0:
            print("Number of files to copy: {}".format(len(sourcelist)))

            # The argument for pool is the number of processors used for the multiprocessing
            p = Pool(1 if args.processors == None else args.processors)

        # functools.partial allows constant parameters to be passed to the Pool
        #	Arguments first positional parm is the function to be performed.
        #	All other paramaters are arguments for the called method
        parmlist = partial(run_sync, sourcedir=_sourcedir, backupdir=_backupdir, syncargs=_syncargs)

        # The map method of the pool takes the method to be iterated and the iterator list as arguments
        p.map(parmlist, sourcelist)
