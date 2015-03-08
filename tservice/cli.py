from __future__ import absolute_import, print_function

import os
import sys
from argparse import ArgumentParser

from .tservice import start_server


def parse_args(args=None):
    description = (
        'Start a Tornado static file server out of a given directory '
        'and with a given prefix. Without a prefix you can browse '
        'your files at http://localhost:8000, with a prefix you would '
        'browse at http://localhost:8000/prefix/.')
    parser = ArgumentParser(description=description)
    parser.add_argument(
        'dir', help='Directory from which to serve files.')
    parser.add_argument(
        '-f', '--prefix', type=str,
        help='A prefix to add to the location from which pages are served.')
    parser.add_argument(
        '-p', '--port', type=int, default=8000,
        help='Port on which to run server.')
    return parser.parse_args(args)


def main(args=None):
    args = parse_args(args)
    os.chdir(args.dir)
    print('Starting server on port {}'.format(args.port))
    if not args.prefix:
        print('Try browsing at http://localhost:{}'.format(args.port))
    else:
        print('Try browsing at http://localhost:{}/{}/'.format(
            args.port, args.prefix))

    try:
        start_server(prefix=args.prefix, port=args.port)
    except KeyboardInterrupt:
        print('')
        print('Goodbye!')
        sys.exit()
