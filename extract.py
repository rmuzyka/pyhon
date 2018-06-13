"""

metoda
podaje dzisiejsza date
ktora wczytuje plik (os)
z niego czyta liste
 
wyrzuca wyjatek jak nie ma pliku
robi jakies regex methods na nim
liczy czas otwarcia pliku
liczy czas wykonania metody
zwraca date pracy nad plikem
testuje metode

"""

import os
import os.path
import sys
import re
import datetime
import time


print '\n\t', 'Today is ', time.asctime(), '\n'


class File(object):
    def __init__(self, file_path):
        self.path = file_path
        self.name = os.path.basename(file_path).upper()

    def __repr__(self):
        return self.name
        # return 'The file name is {} and is located under this path: {}'.format(self.name, self.path)

    def check_is_file(self):
        if os.path.isfile(self.path):
            # print "File exist."
            return True
        else:
            raise IOError
            # print "File does not exist."
            # return False

    def open_file(self):
        try:
            self.check_is_file()
            return open(self.path)
        except IOError:
            print 'Can\'t open. File doesn\'t exist.'

        # try:
        #     return open(self.path)
        #     # if self.check_is_file():
        #     #     return open(self.path)
        # except IOError:
        #     print 'Can\'t open. File doesn\'t exist.'

        # if self.check_is_file():
        #     with open(self.path) as f:
        #         return f

    def read_file(self):
        rf = self.open_file()
        r = rf.read()
        rf.close()
        return r

        # if self.check_is_file():
        #     with open(self.path) as file:
        #         read_data = file.read()
        #         return read_data

    def read_file_line_by_line(self):
            # # read only one line:
            #     test = self.open_file().readline()
            #     print type(test)
            #     print test
        line_list = self.open_file().readlines()
        rfl = [line.strip('\n') for line in line_list]
        return rfl

    def insert_separators_to_string(self, sep = ':'):
        strings = self.read_file_line_by_line()
        macs = []
        for string in strings:
            division = re.split('(\w\w)', string)
            division_without_split_separator = [division[i] for i in range(0, len(division)) if i%2 != 0]
            macs.append(sep.join(division_without_split_separator))
        return macs

    def write_new_string_to_file(self):
        file = open ('new-macs.txt', 'a')
        text = self.insert_separators_to_string()
        for i in text:
            file.writelines(i + '\n')
        file.close()


my_file = File('C:\\Users\\rmuzyka\\my_Pycharm_workspace\\macs.txt')
print 'File name: ', my_file
# my_file.open_file()
print my_file.check_is_file()
print 'from class', my_file.read_file()
print my_file.read_file_line_by_line()
print my_file.insert_separators_to_string()
my_file.write_new_string_to_file()






print '\n\n'
print time.localtime()
print time.asctime()

if os.path.exists('macvs.txt'):
    print "File exist."
else:
    print "File does not exist."

f = open('macs.txt')
print f.read()
f.close()

try:
    print f.read()
except ValueError:
    print 'The file has been closed'

# with open('macs.txt') as macs:
#     read_data = macs.read()
#     for line in read_data:
#         print line
