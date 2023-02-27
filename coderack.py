class Coderack:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, task):
        self.tasks.append(task)
        
    def get_best_task(self):
        best_task = None
        best_score = -float("inf")
        for task in self.tasks:
            score = task.get_score()
            if score > best_score:
                best_score = score
                best_task = task
        return best_task
        
class Task:
    def __init__(self, name):
        self.name = name
        
    def get_score(self):
        return 0

class Metacat:
    def __init__(self):
        self.coderacks = {}
        
    def add_coderack(self, name):
        self.coderacks[name] = Coderack()
        
    def add_task(self, coderack_name, task):
        self.coderacks[coderack_name].add_task(task)
        
    def run(self):
        while True:
            best_task = None
            best_coderack = None
            best_score = -float("inf")
            for coderack_name, coderack in self.coderacks.items():
                task = coderack.get_best_task()
                score = task.get_score()
                if score > best_score:
                    best_task = task
                    best_coderack = coderack_name
                    best_score = score
            if best_task is None:
                break
           
