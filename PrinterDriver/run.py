from DriverFunc import Driver
import os
import time
from datetime import datetime
import shutil
from DriverTools import *




# save the paths 
first_location, second_location = paths()

# define the printer
printer = Driver()

# choose the printer (by asking from user)
for i, j in enumerate(printer.all_printers()):
    print(i,":",j)

choice = int(input("Enter your printer: "))

# set the chosen printer
printer.choose_device(choice)


while True:
    time.sleep(1)
    files = pdf_files(first_location)
    if len(files) > 0:
        for i in files:
            original = first_location + "\\" + i
            target = second_location + "\\" + generate_name(second_location) + '.pdf'
            time.sleep(1)
            while True:
                try:
                    shutil.copyfile(original, target)
                    os.remove(original)
                    printer.print(target)
                    break
                except:
                    continue
