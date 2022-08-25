import os
import time
from datetime import datetime
import shutil


def paths()-> list:
    # return two paths 
    #   1- the path code read pdf files 
    #   2- the path code send printed files
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path.split("\\")[:-1]
    first = dir_path[:]
    second = dir_path[:]
    first.append("TempPdf")
    first = "\\".join(first)

    second.append("PrintedPdf")
    second = "\\".join(second)
    return first, second


def pdf_files(location):
    # return the pdf files in the location
    files = os.listdir(location)
    files = list(filter(lambda x: x[-4:] == '.pdf', files))
    return files

def generate_name(location):
    # generate a name for files
    n = len(pdf_files(location))
    now = str(datetime.now())
    now = "__".join(now.split())
    now = "-".join(now.split(':'))
    now = now.split(".")[0]
    return now + "__" + str(n+1)