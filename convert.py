import csv
import sys
import os

"""Script to convert data from .csv files in directory into strings of values with spaces between them in two lines, example:
1 2 3 4 5 6 7 8 9 10 11
8 7 6 5 4 3 2 1 1 2 3
It is used to convert Tasks data into string to test on site https://nicomedes.assistedcoding.eu/#/app/os/process_scheduling"""

if __name__ == "__main__":

    path = sys.argv[1]

    lines = []

    for file in os.listdir(path):
        with open(os.path.join(path, file), 'r') as f:
            reader = csv.reader(f)
            i = 0
            temp_list = []
            a = []
            t = []
            for line in reader:
                a.append(int(line[0]))
                t.append(int(line[1]))
        temp_list.append(a)
        temp_list.append(t)
        lines.append(temp_list)

    print("Printowanie")
    i = 0
    for line in lines:
        text = ""
        print("Plik " + str(i))
        for array in line:
            for v in array:
                text += str(v) + " "
            text += "\n"
        print(text)
        i += 1
