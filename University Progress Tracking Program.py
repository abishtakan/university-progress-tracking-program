# Date: 13/12/2022

# Initialize variables
Pass = 0
Defer = 0
Fail = 0
progress = 0
trailer = 0
retriever = 0
exclude = 0
option = ""
id = ""
idList = []
passList = []
deferList = []
failList = []
proNameList = []
proCountList = []
proOutcomeList = []
dic ={}
loop1 = True
loop2 = True

# creating / open the text file
file = open("textfile.txt", "w")
file.close()

def validInput(variable):
    """This function takes a string as an argument and returns an integer.
    It asks the user to enter an integer and checks if it is a multiple of 20 and less than or equal to 120.
    If the input is not valid, it asks the user to enter a valid input."""
    while True:
        # error handling for ValueError
        try:
            value = int(input(f"Please enter your credits at {variable}: "))
            if value % 20 == 0 and value <= 120:
                break
            else:
                print("Out of range.")
        except ValueError:
            print("Integer required.")
    return value


def histogram(list1, list2):
    """This function takes two lists as arguments and prints a histogram to the screen."""
    for i in range(len(list1)):
        print(list1[i], list2[i], "\t: " + "*" * list2[i])
    print(f"\n{sum(list2)} outcomes in total")


def List(list1, list2, list3, list4):
    """This function takes 4 lists as arguments and prints them out in a formatted way."""
    for i in range(len(list1)):
        listStatement = f"{list1[i]} - {list2[i]}, {list3[i]}, {list4[i]}"
        print(listStatement)

        # open a text file and append the list outputs in the file
        file = open("textfile.txt", "a")
        file.write(f"{listStatement}\n")


def dictionary(list1, list2, list3, list4, list5):
    """This function takes 5 lists as arguments and returns a dictionary."""
    for i in range(len(list1)):
        dic[list5[i]] = f"{list1[i]} - {list2[i]}, {list3[i]}, {list4[i]}"


def divider(title):
    """This function prints a line of dashes and a title."""
    print("-" * 50)
    print(title)


# print the menu
print("|||||||||| University Progress Tracking Program ||||||||||")
print("\n1. Staff")
print("2. Student")
print("3. Exit")


# get valid option from user
while True:
    option = input("Enter Preferred Option: ")
    if option == "1" or option == "2":
        break
    elif option =="3":
        exit()
    else:
        print("Please Enter valid option\n")

while loop1 is True:
    # get student id, pass credits, defer credits, fail credits from user
    id = input("\nEnter the student ID: ")
    Pass = validInput("Pass")
    Defer = validInput("Defer")
    Fail = validInput("Fail")

    # check the total credits is equal to 120 if that is not equal to 120 then print "Total incorrect" message
    if Pass + Defer + Fail == 120:
        # append student id, pass credits, defer credits, fail credits into respective list
        idList.append(id)
        passList.append(Pass)
        deferList.append(Defer)
        failList.append(Fail)

        # check the credits and print progression outcome, append them into list and count them using if ladder
        if Pass == 120:
            progress += 1
            proOutcomeList.append("Progress")
            print("Progress")
        elif Pass == 100:
            trailer += 1
            proOutcomeList.append("Progress (module trailer)")
            print("Progress (module trailer)")
        elif Pass <= 80 and Fail < 80:
            retriever += 1
            proOutcomeList.append("Module retriever")
            print("Do not progress - module retriever")
        elif Fail >= 80:
            exclude += 1
            proOutcomeList.append("Exclude")
            print("Exclude")

        # check the option and if it is equal t0 "1" then exit the program
        if option == "2":
            exit()
        
        # add progress outcomes name and their count values into respective list
        proNameList = ["Progress", "Trailer", "Retriever", "Exclude"]
        proCountList = [progress, trailer, retriever, exclude]

        # reset the loop2 value as True
        loop2 = True
        print("\nWould you like to enter another set of data?")
        while loop2 is True:
            # get user input for do they need to continue the program or not
            selection = input("Enter 'y' for yes or 'q' to quit and view results: ")
            selection = selection.upper()
            if selection == "Y":
                loop2 = False
            elif selection == "Q":
                loop1 = False
                loop2 = False
            else:
                print("invalid option\n")

    else:
        print("Total incorrect")


# ----------------- Histogram -----------------
divider("Histogram")
histogram(proNameList, proCountList)

# ----------------- Part 2 - List -----------------
divider("Part 2 - List")
List(proOutcomeList, passList, deferList, failList)

# ----------------- Part 3 - Text File -----------------
file = open("textfile.txt", "r")
divider("Part 3 - Text File")
print(file.read(), end="")

# ----------------- Part 4 - Dictionary -----------------
divider("Part 4 - Dictionary")
dictionary(proOutcomeList, passList, deferList, failList, idList)
for key, value in dic.items():      # Reference - https://note.nkmk.me/en/python-dict-keys-values-items/
    print(key,":",value)