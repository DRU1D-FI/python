from Planer import Event, Tasklist, IDManager

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
    mylist.addtask(task1)
    mylist.addtask(task2)
    mylist.addtask(task3)
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

    mylist.delete(3)

    printTasks(tasks)
    
    # next_id = IDManager.get_next_id()

    # print(next_id)
    # print(IDManager.get_next_id())


if __name__ == '__main__':
    main1()
