class AngieTask:
    current_task_id = 0

    def __init__(self,p,ip):
        self.task_port = p
        self.task_ip = ip
        self.task_id = AngieTask.current_task_id
        AngieTask.current_task_id = AngieTask.current_task_id + 1

    def get_port(self):
        return self.task_port

    def get_ip(self):
        return self.task_ip

    def get_id(self):
        return self.task_id
