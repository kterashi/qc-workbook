#!/usr/bin/python3

import os
import sys
import shutil
import subprocess
from argparse import ArgumentParser
from jupyter_book.commands import build

parser = ArgumentParser(description='Build and publish qc-workbook.')
parser.add_argument('--checkout', '-k', action='store_true', dest='checkout', help='Checkout the source files from github.')
parser.add_argument('--account', '-a', metavar='ACCOUNT', dest='account', default='UTokyo-ICEPP', help='Github account of the source repository.')
parser.add_argument('--branch', '-b', metavar='BRANCH', dest='branch', default='master', help='Branch from which to build the website.')
parser.add_argument('--source', '-i', metavar='PATH', dest='source', default='/tmp/qc-workbook/source', help='Source directory.')
parser.add_argument('--target', '-o', metavar='PATH', dest='target', default='/tmp/qc-workbook/build', help='Build directory.')
parser.add_argument('--publish', )
options = parser.parse_args()
sys.argv = []

if options.checkout:
    workdir = os.path.dirname(options.source)
    shutil.rmtree(workdir, ignore_errors=True)
    os.chdir(os.path.dirname(workdir))
    # Can think about installing gitpython if needed
    subprocess.Popen(['git', 'clone', '-b', options.branch, 'https://github.com/{}/qc-workbook'.format(options.account)]).wait()

os.chdir(options.source)

build.callback(path_source='jp',
               path_output=options.target,
               config=None,
               toc=None,
               warningiserror=False,
               nitpick=False,
               keep_going=False,
               freshenv=False,
               builder='html',
               custom_builder=None,
               verbose=0,
               quiet=0,
               individualpages=False)