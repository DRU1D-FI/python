from Planer import Event, Tasklist

def main1():
    number = 1
    print("python main function")
    print(number)
    task1 = Event("20.03.25" , "Math page 15" , "Homework")
    task2 = Event("23.03.25" , "German page 3" , "homework")
    mylist = Tasklist()
    mylist.addtask(task1)
    mylist.addtask(task2)
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
    
    
    for task in tasks:
        print(task.description , task.type , task. date)


if __name__ == '__main__':
    main1()

# from Planer import Saver

# my_list = []
# saver = Saver()

# saver.save("Enter something: ", my_list)
# saver.save("Enter another thing: ", my_list)

# print("Your list:", my_list)