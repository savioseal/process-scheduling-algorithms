class Task:
    """Task class"""

    def __init__(self, id_num, arrival_t, t_to_process):
        self.id = id_num
        self.arrival_time = arrival_t
        self.time_to_process = t_to_process
        self.time_to_process_org = t_to_process
        self.wait_time = 0
        self.turn_around_time = 0
        self.completion_time = -1

    def __repr__(self):
        string = "P" + str(self.id)
        return string

    def __str__(self):
        string = "P" + str(self.id) + " a = " + str(self.arrival_time) + \
            " t = " + str(self.time_to_process)
        return string

    def sort_task_arrival(self):
        return self.arrival_time

    def sort_task_time(self):
        return self.time_to_process
