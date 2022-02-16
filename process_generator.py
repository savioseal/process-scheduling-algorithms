from random import seed
from random import randint
import csv
import os
import sys

"""Small script for generating .csv files filled with data. Data is used for my other script that
simulates processor processing tasks. Data in files is organized as follows: a,t
where A is arrival time (burst time) and t is time to process the task (service time)
Every process is separated by new line

Script is launched as follows:
process_generator.py directory filename num_files tasks_per_file max_arr_time max_proc_time seed_num

- directory: target directory to create files in,
- filename: name of the files. E.Q. files named File will be named File0, File1, File2...
- num_files: number of files to generate
- tasks_per_file: how many tasks a single file will have
- max_arr_time: maximum value of arrival (burst) time the process can have
- max_proc_time: maximum value of (service) time the process can have
- seed_num: seed for random number generator

If launched without arguments, it works on default values"""

if __name__ == "__main__":

    max_val = 100

    if len(sys.argv) == 8:
        path = sys.argv[1]
        filename = sys.argv[2]
        num_files = min(int(sys.argv[3]), max_val)
        tasks_per_file = min(int(sys.argv[4]), max_val)
        max_arr_time = min(int(sys.argv[5]), max_val)
        max_proc_time = min(int(sys.argv[6]), max_val)
        seed_num = int(sys.argv[7])
    else:
        path = 'input'
        filename = 'file'
        tasks_per_file = 10
        num_files = 3
        max_arr_time = 30
        max_proc_time = 19
        seed_num = 1

    text = ""

    #   Create input directory
    if not os.path.exists(path):
        os.makedirs(path)

    seed(seed_num)

    #   Create files and fill them with data
    zero_l = "0"
    for i in range(num_files):
        task_list = []

        if i < 10:
            new_filename = filename + zero_l + str(i) + '.csv'
        else:
            new_filename = filename + str(i) + '.csv'

        with open(os.path.join(path, new_filename), 'w', newline='') as f:
            writer = csv.writer(f)
            for x in range(tasks_per_file):
                task_list.append([])
                arrival_time = randint(0, max_arr_time)
                time_to_process = randint(1, max_proc_time)
                task_list[x].append(arrival_time)
                task_list[x].append(time_to_process)
            writer.writerows(task_list)
