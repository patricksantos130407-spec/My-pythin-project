# ==========================================
# FINAL EXAM PROJECT: PYTHON TUTORIAL APP
# ==========================================

def lesson1():
    print("\n========================================")
    print("       LESSON 1: INTRODUCTION TO PYTHON")
    print("========================================")
    print("Programming means giving instructions to a computer.")
    print("Python is a programming language that is easy to learn.")
    print("It is used to create websites, games, and other programs.")

    print("\nExample:")
    print('print("Hello World")')
    print("Output: Hello World")


def lesson2():
    print("\n========================================")
    print("       LESSON 2: BASIC INPUT & OUTPUT")
    print("========================================")
    print("The input() function is used to get information.")
    print("The print() function is used to display information.")

    name = input("\nEnter your name: ")
    age = input("Enter your age: ")

    print("\nHello", name)
    print("You are", age, "years old.")


def lesson3():
    print("\n========================================")
    print("       LESSON 3: SYNTAX & VARIABLES")
    print("========================================")
    print("Variables are used to store information.")

    name = "Patrick"
    score = 95
    is_passing = True

    print("Name:", name)
    print("Score:", score)
    print("Passing:", is_passing)

    print("\nComments are written using the # symbol.")


def lesson4():
    print("\n========================================")
    print("       LESSON 4: ARITHMETIC OPERATORS")
    print("========================================")
    print("Enter two numbers to perform basic math.")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nAddition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    if num2 != 0:
        print("Division:", num1 / num2)
        print("Floor Division:", num1 // num2)
        print("Modulus:", num1 % num2)
    else:
        print("Cannot divide by zero.")

    print("Exponent:", num1 ** num2)


def lesson5():
    print("\n========================================")
    print("       LESSON 5: CONDITIONAL STATEMENTS")
    print("========================================")

    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age.")
    elif age <= 12:
        print("You are a child.")
    elif age <= 19:
        print("You are a teenager.")
    elif age <= 59:
        print("You are an adult.")
    elif age <= 120:
        print("You are a senior citizen.")
    else:
        print("Invalid age.")


def lesson6():
    print("\n========================================")
    print("       LESSON 6: LOGICAL OPERATORS")
    print("========================================")
    print("Logical operators are AND, OR, and NOT.")

    age = int(input("Enter your age: "))
    student = input("Are you a student? (yes/no): ")

    if age < 0 or age > 120:
        print("Invalid age.")
    else:
        gets_discount = age < 18 or age >= 60 or student.lower() == "yes"

        print("Eligible for discount:", gets_discount)


def lesson7():
    print("\n========================================")
    print("       LESSON 7: LOOPS")
    print("========================================")

    print("\nFOR LOOP")
    for x in range(1, 6):
        print(x)

    print("\nWHILE LOOP")
    count = 3

    while count > 0:
        print(count)
        count -= 1

    print("Finished!")


def main():
    running = True

    while running:
        print("\n========================================")
        print("          PYTHON TUTORIAL APP")
        print("========================================")
        print("[1] Introduction to Python")
        print("[2] Basic Input and Output")
        print("[3] Syntax and Variables")
        print("[4] Arithmetic Operators")
        print("[5] Conditional Statements")
        print("[6] Logical Operators")
        print("[7] Loops")
        print("[8] Exit")
        print("========================================")

        choice = input("Choose a lesson (1-8): ")

        if choice == "1":
            lesson1()
        elif choice == "2":
            lesson2()
        elif choice == "3":
            lesson3()
        elif choice == "4":
            lesson4()
        elif choice == "5":
            lesson5()
        elif choice == "6":
            lesson6()
        elif choice == "7":
            lesson7()
        elif choice == "8":
            print("Thank you for using my Python Tutorial App!")
            running = False
        else:
            print("Invalid choice. Please try again.")


main()
