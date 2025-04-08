from datetime import datetime, timedelta,date

class Event:

    def __init__(self, date: date, description, type):
        self.date = date
        self.description = description
        self.type = type
        self.id = IDManager.get_next_id()

class Tasklist:
    def __init__(self):
        self.tasklist = []
        return

    def gettasks(self):
        return self.tasklist


    def addtask(self, task: Event): 
        self.tasklist.append(task)
        return
    


    def delete(self, id):

        for i in range(len(self.tasklist)):
            task = self.tasklist[i]
            if task.id == id:
                self.tasklist.pop(i)

        # for task in self.tasklist:
        #     if task.id == id:
        #         self.tasklist.remove(task)
        #     return
        
    def weeklyTasks(self):
        today = datetime.today().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)


        return [task for task in self.tasklist if start_of_week <= task.date <= end_of_week]
    
class Saver:
    def save(self, message, user_list):
        user_input = input(message)
        user_list.append(user_input)

class IDManager:
    next_id = 1 

    @classmethod
    def get_next_id(cls):
        assigned_id = cls.next_id  
        cls.next_id += 1  
        return assigned_id

