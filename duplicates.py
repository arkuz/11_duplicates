import os
import argparse
import sys
from collections import Counter


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('dirpath', help='Path to directory')
    return parser


def get_files_info_list(directory):
    files_info_list = {}
    for path, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(path, filename)
            filesize = os.path.getsize(filepath)
            files_info_list.setdefault(
                (filename, filesize), []).append(filepath)
    return files_info_list


def get_duplicate_list(files_info_list):
    duplicate_list = []
    for paths in files_info_list.values():
        if len(paths) > 1:
            for path in paths:
                duplicate_list.append(path)
    return duplicate_list


def print_duplicate_list(duplicate_list):
    print('Duplicate files:')
    for path in duplicate_list:
        print('  {}'.format(path))


if __name__ == '__main__':

    parser = create_arg_parser()
    args = parser.parse_args()
    dirpath = os.path.abspath(args.dirpath)

    if not os.path.isdir(dirpath):
        sys.exit('The path is not a directory.')

    files_list = get_files_info_list(dirpath)

    duplicate_list = get_duplicate_list(files_list)
    if not duplicate_list:
        print('Duplicate files not exist.')

    print_duplicate_list(duplicate_list)
