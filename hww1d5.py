#1. The Calculator App
# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.
calculator = []
def decide():
    while True:
        user_choice = input("What function will you be using: add, subtract, multiply, or divide? type 'quit' to quit: ")
        if user_choice == ("add"):
            choice3()
            break
        elif user_choice == ("subtract"):
            choice4()
            break
        elif user_choice == ("multiply"):
            choice2()
            break
        elif user_choice == ("divide"):
            choice()
            break
        elif user_choice == ('quit'):
            break
        else:
            print("Invalid entry, try again!")

def choice():
    while True:
        try:
            number = int(input("Enter the first number:"))
            number2 = int(input("Enter the second number:"))
            result = number / number2
            print(result)
            break
        except ZeroDivisionError:
            print("HUHH? you can't divide by zero.. -.-")
            continue
        except (TypeError, ValueError):
            print("invalid entry!")
            continue
    
def choice2():
    while True:
        try:
            number = int(input("Enter the first number:"))
            number2 = int(input("Enter the second number:"))
            result = number * number2
            print(result)
            break
        except (TypeError, ValueError):
            print("invalid entry!")
            continue

def choice3():
    while True:
        try:
            number = int(input("Enter the first number:"))
            number2 = int(input("Enter the second number:"))
            result = number + number2
            print(result)
            break
        except (TypeError, ValueError):
            print("invalid entry!")
            continue

def choice4():
    while True:
        try:
            number = int(input("Enter the first number:"))
            number2 = int(input("Enter the second number:"))
            result = number - number2
            print(result)
            break
        except (TypeError, ValueError):
            print("invalid entry!")
            continue
decide()

# 2. The Shopping List Maker
# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.

shopping_list = [ ]
removed_items = [ ]

def adding():
    while True:
        user_input = input("Add item: type 'done' when done. ")
        if user_input == "done":
            print("LETS GO SHOPPING!")
            break
        else:
            shopping_list.append(user_input)

def my_list():
    print("This is your list so far!")
    for items in shopping_list:
        print(items)

def removing():
    while True:
        user_input = input("Type the item you want to remove. ")
        if user_input == "done":
            print(f"You are done removing items!")
            break
        else:
            shopping_list.remove(user_input)
            removed_items.append(user_input)
            print(f"You successfully removed {removed_items}!")
adding()
my_list()
removing()
my_list()

# 3. The Grade Analyzer
# Task 1: Code a function to calculate the average grade.
# Task 2: Implement a function to find the highest and lowest grade.
# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
grades = [50, 51, 67, 65, 54, 65, 80, 80, 91, 89, 98, 97]
letter_grades = [ ]
def avg(grades):
    total = sum(grades)
    return total / len(grades)

def hi_lo(grades):
    highest = max(grades)
    lowest = min(grades)
    return [lowest, highest]
  
def letter(grades):
    for grade in grades:
        if grade >= 90:
            letter_grades.append("A")
        elif grade >= 80:
            letter_grades.append("B")
        elif grade >= 70:
            letter_grades.append("C")
        elif grade >= 60:
            letter_grades.append("D")
        else:
            letter_grades.append("F")
    return letter_grades

print(avg(grades))
print(hi_lo(grades))  
print(letter(grades))

