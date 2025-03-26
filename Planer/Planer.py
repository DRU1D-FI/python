class Event:
    def __init__(self, date, description, type):
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
        return


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
