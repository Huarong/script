#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import cPickle as pickle
import pprint


def parse_cmd_args():
    parser = argparse.ArgumentParser(description='Read and print the python pickle file')
    parser.add_argument('file', help='python pickle file path')
    args = parser.parse_args()
    file_path = os.path.abspath(args.file)
    return file_path


def main():
    file_path = parse_cmd_args()
    with open(file_path) as f:
        obj = pickle.load(f)
    pprint.pprint(obj)
    return None


if __name__ == '__main__':
    main()
