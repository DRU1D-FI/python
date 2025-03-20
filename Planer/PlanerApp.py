from Planer import Event

def main1():
    number = 1
    print("python main function")
    print(number)
    task1 = Event("20.03.25" , "Math page 15" , "Homework")
    date = input("Enter the date: ")
    description = input("Enter the description:")
    type = input("enter the type: ")
    print(date , description , type)
    print("===========")
    task = Event(date , description , type)
    tasklist = []
    tasklist.append(task)
    tasklist.append(task1)
    
    for task in tasklist:
        print(task.date , task.description , task.type)


if __name__ == '__main__':
    main1()