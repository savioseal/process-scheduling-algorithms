from task import Task
import copy


class TaskProcessor:
    """TaskProcessor class. Calculates algorithms when provided Task objects"""

    def __init__(self):
        self.is_busy = False
        self.current_task = None

    #   Operates on given tasks using SJF algorithm and returns them as a list
    def shortest_job_first(self, incoming_tasks: list[Task]) -> list[Task]:
        time = 0
        incoming_tasks_sorted = sorted(copy.deepcopy(
            incoming_tasks), key=lambda x: (x.time_to_process, x.arrival_time))
        arrival_first = sorted(incoming_tasks_sorted, key=lambda x: (
            x.arrival_time, x.time_to_process))
        tasks_done = []
        #   Find first task
        self.current_task = incoming_tasks_sorted.pop(
            incoming_tasks_sorted.index(arrival_first[0]))
        time = self.current_task.arrival_time
        self.is_busy = True

        while self.is_busy:
            #   Change current task if it's done being processed
            if self.current_task.time_to_process <= 0:
                self.current_task.completion_time = time
                self.current_task.turn_around_time = time - self.current_task.arrival_time
                self.current_task.wait_time = time - \
                    self.current_task.time_to_process_org - self.current_task.arrival_time
                tasks_done.append(self.current_task)
                #   If there are incoming tasks, put the shortest in the current_task
                if incoming_tasks_sorted:
                    found = False
                    for task in incoming_tasks_sorted:
                        if task.arrival_time <= time:
                            self.current_task = incoming_tasks_sorted.pop(
                                incoming_tasks_sorted.index(task))
                            found = True
                            break
                    #   If there is empty time period between tasks, find the closest one to arrive and skip time there
                    if not found:
                        arrival_first = sorted(incoming_tasks_sorted, key=lambda x: (
                            x.arrival_time, x.time_to_process))
                        self.current_task = arrival_first[0]
                        incoming_tasks_sorted.pop(
                            incoming_tasks_sorted.index(arrival_first[0]))
                        time = self.current_task.arrival_time
                        continue
                #   End the loop when all tasks got processed
                elif len(tasks_done) == len(incoming_tasks):
                    self.current_task = None
                    self.is_busy = False
                    break
            time += self.current_task.time_to_process
            self.current_task.time_to_process = 0

        return tasks_done

    #   Operates on given tasks using FCFS algorithm and returns them as a list
    def first_come_first_serve(self, incoming_tasks: list[Task]) -> list[Task]:
        incoming_tasks_sorted = sorted(copy.deepcopy(
            incoming_tasks), key=Task.sort_task_arrival)
        tasks_done = []
        #   Get first task
        self.current_task = incoming_tasks_sorted.pop(0)
        time = self.current_task.arrival_time

        self.is_busy = True

        while self.is_busy:
            #   Change current task if it's done being processed
            if self.current_task.time_to_process <= 0:
                self.current_task.completion_time = time
                self.current_task.turn_around_time = time - self.current_task.arrival_time
                self.current_task.wait_time = time - \
                    self.current_task.time_to_process_org - self.current_task.arrival_time
                tasks_done.append(self.current_task)
                #   If there are incoming tasks, put the next one as current task
                if incoming_tasks_sorted:
                    self.current_task = incoming_tasks_sorted.pop(0)
                    if self.current_task.arrival_time > time:
                        time = self.current_task.arrival_time
                #   End the loop when all tasks got processed
                elif len(tasks_done) == len(incoming_tasks):
                    self.current_task = None
                    self.is_busy = False
                    break
            time += self.current_task.time_to_process
            self.current_task.time_to_process = 0

        return tasks_done
