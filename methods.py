import os
from os import listdir
from os.path import isfile, join

def get_files(path):
    cwd = os.getcwd()
    onlyfiles = [os.path.join(cwd, f) for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]
    print onlyfiles

get_files('C:\P5-6\test.txt')

