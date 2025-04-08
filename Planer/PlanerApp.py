from Planer import Event, Tasklist, IDManager
from datetime import date

def printTasks(tasks):
    for task in tasks:
        print(task.description , task.type , task.date ,task.id)

def main1():
    number = 1
    print("python main function")
    print(number)
    task1 = Event("20.03.25" , "Math page 15" , "Homework")
    task2 = Event("23.03.25" , "German page 3" , "homework")
    task3 = Event("24.03.25" , "french" , "homework")
    mylist = Tasklist()
    # mylist.addtask(task1)
    # mylist.addtask(task2)
    # mylist.addtask(task3)
    mylist.addtask(Event(date(2025, 4, 9), "WAH", "test"))
    mylist.addtask(Event(date(2025, 4, 3), "english", "test"))
    mylist.addtask(Event(date(2025, 4, 13), "NT", "test"))  # Next week

    # date = input("Enter the date: ")
    # description = input("Enter the description:")
    # type = input("enter the type: ")
    # print(date , description , type)
    # print("===========")
    # task = Event(date , description , type)
    # tasklist = []
    # tasklist.append(task)
    # tasklist.append(task1)
    tasks = mylist.gettasks()
        
    printTasks(tasks)

    # mylist.delete(3)

    # printTasks(tasks)
    print("======================")
    for task in mylist.weeklyTasks(): 
        print(f"{task.date} - {task.description} ({task.type})")
   
    # next_id = IDManager.get_next_id()

    # print(next_id)
    # print(IDManager.get_next_id())


if __name__ == '__main__':
    main1()
