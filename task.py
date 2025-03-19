def main():
    print ("|X-----------<****************>------------X|")
    print ("|------------<* TASK MANAGER *>-------------|")
    print ("|X-----------<****************>------------X|")
    print ("|                                           |")
    print ("|       1. ADD A TASK                       |")
    print ("|       2. ADD A STEP TO A TASK             |")
    print ("|       3. MARK STEP AS COMPLETE            |")
    print ("|       4. VIEW ALL TASKS                   |")
    print ("|       5. REMOVE A TASK                    |")
    print ("|       6. DISPLAY TOTAL NUMBER OF TASKS    |")
    print ("|       7. QUIT                             |\n")

    tasks = {}

    while True:
        def one():
            key = input("Please enter the task you'd like to add: ")
            tasks[key] = key
            print ("Successfully added task.\n")

        def two():
            key = input("Please enter the task you'd like to add a step to: ")
            step = input("Enter the step to be added: ")
            try:
                tasks[key] = step
                print ("Successfully added step.\n")
            except KeyError:
                print ("Please enter a valid task.")

        def three():
            key = input("Please enter the task you'd like to mark as done: ")
            try:
                tasks[key] = "[DONE]"
                print ("Successfully completed step.\n")
            except KeyError:
                print ("Please enter a valid task.")

        def four():
            print (tasks, "\n")

        def five():
            key = input("Please enter the task you'd like to remove: ")
            try:
                del tasks[key]
                print ("Successfully deleted task.\n")
            except KeyError:
                print ("Please enter a valid task.")

        def six():
            print(len(tasks), "\n")

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

main()