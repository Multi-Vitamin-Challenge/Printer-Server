import os
import json


def question_folder_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path.split("\\")[:-1]
    dir_path.append("Questions")
    return "\\".join(dir_path)

def question_folder_classes():
    rootdir = question_folder_path()
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            yield d

def pdf_files_of_address(address):
    for file in os.listdir(address):
        if file[-4:]==".pdf":
            yield file

def question_folder_structur():
    output = dict()
    for address in question_folder_classes():
        temp_address = address.split("\\")[-1]
        output[temp_address] = list(pdf_files_of_address(address))

    return output

def username_password():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dir_path = dir_path.split("\\")[:-1]
    dir_path.append("Config")
    dir_path.append("config.json")
    address =  "\\".join(dir_path)

    with open(address) as d:
        dictData = json.load(d)
    return dictData

if __name__ == "__main__":
    #print(question_folder_path())
#    a = list(question_folder_classes())
#    print(list(pdf_files_of_address(a[0])))
#    print(question_folder_structur())
    print(username_password())