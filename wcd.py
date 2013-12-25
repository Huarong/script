#! /usr/bin/python
# -*- coding: utf-8 -*-

# wcd
# A linux script like bash script wc with the feature of counting recursively


import os
import os.path
import argparse
import Queue as queue
import subprocess


def parse_cmd_args():
    parser = argparse.ArgumentParser(description='word count of all the files in a directory')
    parser.add_argument('name', nargs='*', help='the name of the directory or file to be count')
    args = parser.parse_args()
    return args.name


class WordCounter(object):
    def __init__(self, filename):
        self.to_count_dir = queue.Queue()
        self.file_list = []
        self.init_files = filename
        self.__clean_init_files()

    def __clean_init_files(self):
        # count all the files and directories in the current working directory
        if not self.init_files:
            self.init_files = [os.getcwd()]
        self.init_files = (os.path.abspath(d) for d in self.init_files)
        for e in self.init_files:
            if os.path.isdir(e):
                self.to_count_dir.put(e)
            else:
                self.file_list.append(e)
        return None

    def __list_a_dir(self):
        # get a directory from queue to_count_dir
        # get the absolute path of all files and directories in this directory
        a_dir = self.to_count_dir.get()
        fs = [os.path.join(a_dir, f) for f in os.listdir(a_dir)]
        for f in fs:
            # put directories into to_count_dir
            if os.path.isdir(f):
                self.to_count_dir.put(f)
            else:
                self.file_list.append(f)
        return None

    def get_all_filenames(self):
        while not self.to_count_dir.empty():
            self.__list_a_dir()
        return None

    def count_line(self):
        cmd = ['wc', '-l'] + self.file_list
        subprocess.call(cmd)


def main():
    directories = parse_cmd_args()
    wc = WordCounter(directories)
    wc.get_all_filenames()
    wc.count_line()
    return None


if __name__ == '__main__':
    main()
