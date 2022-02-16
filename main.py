from task import Task
from taskprocessor import TaskProcessor
import csv
import os
import copy
import timeit
import sys

"""Script for simulating process scheduling. Calculates total service time, 
average turn around time, average waiting time, and other data.

Input arguments:
input directory with .csv files in it
output directory

If no arguments are given, the default input and output are "input" and "results"

Output data is in .csv format"""

if __name__ == "__main__":

    path = 'input'
    output_path = 'results'

    if len(sys.argv) == 3:
        path = sys.argv[1]
        output_path = sys.argv[2]

    if not os.path.exists(path):
        os.makedirs(path)

    proc = TaskProcessor()

    input_list = []
    task_list = []

    #   Read files from input directory
    i = 0
    for file in os.listdir(path):
        with open(os.path.join(path, file), 'r') as f:
            reader = csv.reader(f)
            temp_list2 = []

            for line in reader:
                temp_list = []
                for v in line:
                    temp_list.append(int(v))
                temp_list2.append(Task(i, temp_list[0], temp_list[1]))
                i += 1
            input_list.append(temp_list2)

    task_list = copy.deepcopy(input_list)

    output_list_sjf = []
    output_list_fcfs = []

    header1 = ["Task ID", "Arrival time", "Service time",
               "Completion time", "Turn around time", "Wait time"]

    total_tasks_str = "\nTotal tasks: "
    total_service_str = "Total service time for all processes: "
    av_tat_str = "Average turnaround time: "
    av_wat_str = "Average waiting time: "
    elapsed_time_str = "Elapsed time: "
    av_total_service_str = "Average total service time for all tests: "
    av_total_tat_str = "Average turnaround time per test: "
    av_total_wat_str = "Average waiting time per test: "
    av_elapsed_time_str = "Average elapsed time per test: "
    av_total_service = 0
    av_total_tat = 0
    av_total_wat = 0
    av_elapsed_time = 0

    print("START")

    # SJF
    file_count = 0
    for line in task_list:
        file_count_str = ["File " + str(file_count)]

        #   Start counting algorithm processing time
        starttime_sjf = timeit.default_timer()

        result = proc.shortest_job_first(line)

        #   Stop counting algorithm processing time
        endtime_sjf = timeit.default_timer()

        result_time = 0
        av_tat = 0
        av_wat = 0
        total_tasks = len(result)

        output_list_sjf.append(["SJF"])
        output_list_sjf.append(file_count_str)
        output_list_sjf.append(header1)

        for task in result:
            av_tat += task.turn_around_time
            av_wat += task.wait_time
            result_time += task.time_to_process_org

            output_list_sjf.append([task.id, task.arrival_time, task.time_to_process_org,
                                    task.completion_time, task.turn_around_time, task.wait_time])
        av_tat = av_tat/total_tasks
        av_wat = av_wat/total_tasks

        #   Counting for results of all tests
        av_total_service += result_time
        av_total_tat += av_tat
        av_total_wat += av_wat
        av_elapsed_time += round(endtime_sjf-starttime_sjf, 4)

        output_list_sjf.append([total_tasks_str, total_tasks])
        output_list_sjf.append([total_service_str, result_time])
        output_list_sjf.append([av_tat_str, av_tat])
        output_list_sjf.append([av_wat_str, av_wat])
        output_list_sjf.append(
            [elapsed_time_str, round(endtime_sjf-starttime_sjf, 4)])
        output_list_sjf.append([])

        file_count += 1

    av_total_service = round(av_total_service/(file_count), 1)
    av_total_tat = round(av_total_tat/(file_count), 1)
    av_total_wat = round(av_total_wat/(file_count), 1)
    av_elapsed_time = round(av_elapsed_time/(file_count), 4)

    output_list_sjf.append([av_total_service_str, av_total_service])
    output_list_sjf.append([av_total_tat_str, av_total_tat])
    output_list_sjf.append([av_total_wat_str, av_total_wat])
    output_list_sjf.append([av_elapsed_time_str, av_elapsed_time])

    av_total_service = 0
    av_total_tat = 0
    av_total_wat = 0
    av_elapsed_time = 0

    # FCFS
    file_count = 0
    for line in task_list:
        file_count_str = ["File " + str(file_count)]

        #   Start counting algorithm processing time
        starttime_fcfs = timeit.default_timer()

        result = proc.first_come_first_serve(line)

        #   Stop counting algorithm processing time
        endtime_fcfs = timeit.default_timer()

        result_time = 0
        av_tat = 0
        av_wat = 0
        total_tasks = len(result)

        output_list_fcfs.append(["FCFS"])
        output_list_fcfs.append(file_count_str)
        output_list_fcfs.append(header1)

        for task in result:
            av_tat += task.turn_around_time
            av_wat += task.wait_time
            result_time += task.time_to_process_org
            output_list_fcfs.append([task.id, task.arrival_time, task.time_to_process_org,
                                    task.completion_time, task.turn_around_time, task.wait_time])
        av_tat = av_tat/total_tasks
        av_wat = av_wat/total_tasks

        #   Counting for results of all tests
        av_total_service += result_time
        av_total_tat += av_tat
        av_total_wat += av_wat
        av_elapsed_time += round(endtime_sjf-starttime_sjf, 4)

        output_list_fcfs.append([total_tasks_str, total_tasks])
        output_list_fcfs.append([total_service_str, result_time])
        output_list_fcfs.append([av_tat_str, av_tat])
        output_list_fcfs.append([av_wat_str, av_wat])
        output_list_fcfs.append(
            [elapsed_time_str, round(endtime_fcfs-starttime_fcfs, 4)])
        output_list_fcfs.append([])

        file_count += 1

    av_total_service = round(av_total_service/(file_count), 1)
    av_total_tat = round(av_total_tat/(file_count), 1)
    av_total_wat = round(av_total_wat/(file_count), 1)
    av_elapsed_time = round(av_elapsed_time/(file_count), 4)

    output_list_fcfs.append([av_total_service_str, av_total_service])
    output_list_fcfs.append([av_total_tat_str, av_total_tat])
    output_list_fcfs.append([av_total_wat_str, av_total_wat])
    output_list_fcfs.append([av_elapsed_time_str, av_elapsed_time])

    av_total_service = 0
    av_total_tat = 0
    av_total_wat = 0
    av_elapsed_time = 0

    list_of_outputs = [output_list_sjf, output_list_fcfs]

    #   Writing results to file
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    count = 0
    for item in list_of_outputs:
        output_file = 'results' + str(count) + '.csv'
        with open(os.path.join(output_path, output_file), 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerows(item)
        count += 1

    print("END")
