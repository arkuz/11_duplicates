import os
import argparse
import sys
from collections import Counter


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('dirPath', help='Path to directory')
    return parser


def get_files_info_list(directory):
    files_info_list = []
    for path, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(path, filename)
            filesize = os.path.getsize(filepath)
            files_info_list.append(
                (
                    os.path.normpath(filepath),
                    filename,
                    filesize
                )
            )
    return files_info_list


def get_files_info_without_path_list(short_files_list):
    files_info_list = []
    for _, filename, filesize in short_files_list:
        files_info_list.append((filename, filesize))
    return files_info_list


def find_duplicate(short_list):
    duplicate_list = [
        k for k, count in Counter(short_list).items() if count > 1
    ]
    return duplicate_list


def print_duplicate_list(full_files_list, duplicate_list):
    print('Duplicate files:')
    for filepath, filename, filesize in full_files_list:
        for fname, fsize in duplicate_list:
            if filename == fname and filesize == fsize:
                print('  {0}'.format(filepath))


if __name__ == '__main__':

    parser = create_arg_parser()
    args = parser.parse_args()
    dirpath = os.path.abspath(args.dirPath)

    if not os.path.isdir(dirpath):
        sys.exit('The path is not a directory.')

    full_files_list = get_files_info_list(dirpath)

    short_files_list = get_files_info_without_path_list(full_files_list)

    duplicate_list = find_duplicate(short_files_list)

    print_duplicate_list(full_files_list, duplicate_list)
