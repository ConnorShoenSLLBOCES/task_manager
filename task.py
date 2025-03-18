print ("|}X----------<****************>-----------X{|")
print ("|}-----------<* TASK MANAGER *>------------{|")
print ("|}X----------<****************>-----------X{|")
print ("|                                           |")
print ("|       1. ADD A TASK                       |")
print ("|       2. ADD A STEP TO A TASK             |")
print ("|       3. MARK TASK AS COMPLETE            |")
print ("|       4. VIEW ALL TASKS                   |")
print ("|       5. REMOVE A TASK                    |")
print ("|       6. DISPLAY TOTAL NUMBER OF TASKS    |")
print ("|       7. QUIT                             |\n")

while True:
    tasks = {}

    def one():
        key = input("Please enter the task you'd like to add: ")
        tasks[key] = 1
        print ("Successfully added task.\n")

    def two():
        key = input("Please enter the task you'd like to add a step to: ")
        try:
            step = input("Enter the step to be added: ")
            tasks[key].apend(step)
        except KeyError:
            print ("Please enter a valid task.")
        print ("Successfully added step.\n")

    def three():
        key = input("Please enter the task you'd like to mark as done: ")
        try:
            del tasks[key]
        except KeyError:
            print ("Please enter a valid task.")
        print ("Successfully completed task.\n")

    def four():
        print (tasks, "\n")

    def five():
        key = input("Please enter the task you'd like to remove: ")
        del tasks[key]
        print ("\n")

    def six():
        print(tasks.values(), "\n")

    choice = input("Please enter the number of what you'd like to do: ")

    if choice == "1":
        one()
    elif choice == "2":
        two()
    elif choice == "3":
        three()
    elif choice == "4":
        four()
    elif choice == "5":
        five()
    elif choice == "6":
        six()
    elif choice == "7":
        print("Thank you for using the task manager!")
        break
    else:
        print("Sorry, that's not one of the options. Please try again.\n")