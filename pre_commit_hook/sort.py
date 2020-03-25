from __future__ import print_function

import argparse
import os

from isort import isort


def imports_incorrect(filename, show_diff=False, **options):
    return isort.SortImports(filename, check=True, show_diff=show_diff, **options).incorrectly_sorted


def main(argv=None):

    # `black` suggested config:
    # https://black.readthedocs.io/en/stable/the_black_code_style.html
    options = {
            'multi_line_output': 3,
            'include_trailing_comma': True,
            'force_grid_wrap': 0,
            'use_parentheses': True,
            'line_length': 88
            }

    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to run')
    parser.add_argument('--silent-overwrite', action='store_true', dest='silent', default=False)
    parser.add_argument('--check-only', action='store_true', dest='check_only', default=False)
    parser.add_argument('--diff', action='store_true', dest='show_diff', default=False)
    args = parser.parse_args(argv)

    return_value = 0

    for filename in args.filenames:
        if imports_incorrect(filename, show_diff=args.show_diff, **options):
            if args.check_only:
                return_value = 1
            elif args.silent:
                isort.SortImports(filename, **options)
            else:
                return_value = 1
                isort.SortImports(filename, **options)
                print('FIXED: {0}'.format(os.path.abspath(filename)))
    return return_value

if __name__ == '__main__':
    exit(main())
