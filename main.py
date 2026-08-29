import datetime
import time
import math
import random
import uuid

from mytools import file_operations
from mytools import math_utils


# DATETIME AND TIME OPERATIONS

def datetime_menu():
    
    while True:

        print("\n========================")
        print("Datetime and Time Operations")
        print("========================")

        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            current_time = datetime.datetime.now()

            print(
                "\nCurrent Date and Time:",
                current_time.strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            )

        elif choice == "2":

            first_date = input(
                "\nEnter the first date (YYYY-MM-DD): "
            )

            second_date = input(
                "Enter the second date (YYYY-MM-DD): "
            )

            try:

                date1 = datetime.datetime.strptime(
                    first_date,
                    "%Y-%m-%d"
                )

                date2 = datetime.datetime.strptime(
                    second_date,
                    "%Y-%m-%d"
                )

                difference = abs(
                    (date2 - date1).days
                )

                print(
                    "Difference:",
                    difference,
                    "days"
                )

            except ValueError:

                print("Invalid date format!")

        elif choice == "3":

            current_date = datetime.datetime.now()

            print("\nCustom Date Formats:")

            print(
                "DD-MM-YYYY:",
                current_date.strftime(
                    "%d-%m-%Y"
                )
            )

            print(
                "DD/MM/YYYY:",
                current_date.strftime(
                    "%d/%m/%Y"
                )
            )

            print(
                "Month Day Year:",
                current_date.strftime(
                    "%B %d, %Y"
                )
            )

        elif choice == "4":

            print("\nStopwatch Started!")

            print(
                "Press ENTER to stop."
            )

            start_time = time.time()

            input()

            end_time = time.time()

            total_time = end_time - start_time

            print(
                "Time:",
                round(total_time, 2),
                "seconds"
            )

        elif choice == "5":

            seconds = int(
                input(
                    "\nEnter countdown seconds: "
                )
            )

            print("\nCountdown Started!")

            while seconds > 0:

                print(seconds)

                time.sleep(1)

                seconds = seconds - 1

            print("Time's Up!")

        elif choice == "6":

            break

        else:

            print("Invalid choice!")


# MATHEMATICAL OPERATIONS

def mathematical_menu():
    '''
    This function displays the Mathematical Operations menu.
    Mathematical functions are imported from math_utils.py.
    '''
    while True:

        print("\n========================")
        print("Mathematical Operations")
        print("========================")

        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            math_utils.factorial()

        elif choice == "2":

            math_utils.compound_interest()

        elif choice == "3":

            math_utils.trigonometry()

        elif choice == "4":

            math_utils.area_of_shapes()

        elif choice == "5":

            break

        else:

            print("Invalid choice!")

# RANDOM DATA GENERATION

def random_menu():
       while True:

        print("\n========================")
        print("Random Data Generation")
        print("========================")

        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            start = int(
                input(
                    "\nEnter starting number: "
                )
            )

            end = int(
                input(
                    "Enter ending number: "
                )
            )

            number = random.randint(
                start,
                end
            )

            print(
                "Random Number:",
                number
            )

        elif choice == "2":

            start = int(
                input(
                    "\nEnter starting number: "
                )
            )

            end = int(
                input(
                    "Enter ending number: "
                )
            )

            size = int(
                input(
                    "Enter list size: "
                )
            )

            random_list = []

            for i in range(size):

                number = random.randint(
                    start,
                    end
                )

                random_list.append(
                    number
                )

            print(
                "Random List:",
                random_list
            )

        elif choice == "3":

            length = int(
                input(
                    "\nEnter password length: "
                )
            )

            characters = (
                "abcdefghijklmnopqrstuvwxyz"
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                "0123456789"
                "!@#$%^&*"
            )

            password = ""

            for i in range(length):

                password = password + random.choice(
                    characters
                )

            print(
                "Generated Password:",
                password
            )

        elif choice == "4":

            otp = random.randint(
                100000,
                999999
            )

            print(
                "Generated OTP:",
                otp
            )

        elif choice == "5":

            break

        else:

            print("Invalid choice!")


# UUID

def generate_uuid():
    '''
    This function generates a unique identifier
    using the UUID module.
    '''

    print("\n========================")
    print("Generate Unique Identifiers")
    print("========================")

    unique_id = uuid.uuid4()

    print(
        "Generated UUID:",
        unique_id
    )


# FILE OPERATIONS

def file_menu():
    '''
    This function displays the File Operations menu.

    The actual file functions are imported from
    the custom file_operations module.
    '''

    while True:

        print("\n========================")
        print("File Operations")
        print("========================")

        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            file_operations.create_file()

        elif choice == "2":

            file_operations.write_file()

        elif choice == "3":

            file_operations.read_file()

        elif choice == "4":

            file_operations.append_file()

        elif choice == "5":

            break

        else:

            print("Invalid choice!")


# DIR() FUNCTION

def explore_module():
    '''
    This function demonstrates the dir() function.

    dir() returns the available attributes and
    functions inside a module.
    '''

    print("\n========================")
    print("Explore Module Attributes")
    print("========================")

    module_name = input(
        "Enter module name to explore: "
    )

    if module_name == "math":

        print(
            "\nAvailable Attributes in math module:"
        )

        print(dir(math))

    elif module_name == "random":

        print(
            "\nAvailable Attributes in random module:"
        )

        print(dir(random))

    elif module_name == "datetime":

        print(
            "\nAvailable Attributes in datetime module:"
        )

        print(dir(datetime))

    elif module_name == "time":

        print(
            "\nAvailable Attributes in time module:"
        )

        print(dir(time))

    else:

        print(
            "Module not available in this project."
        )


# MAIN MENU

def main():
    '''
    This function displays the Main Menu.

    The user can select different operations
    from the menu.
    '''

    while True:

        print("\n")
        print("==========================")
        print("Welcome to Multi-Utility Toolkit")
        print("==========================")

        print("Choose an option:")

        print(
            "1. Datetime and Time Operations"
        )

        print(
            "2. Mathematical Operations"
        )

        print(
            "3. Random Data Generation"
        )

        print(
            "4. Generate Unique Identifiers (UUID)"
        )

        print(
            "5. File Operations (Custom Module)"
        )

        print(
            "6. Explore Module Attributes (dir())"
        )

        print(
            "7. Exit"
        )

        print("==========================")

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            datetime_menu()

        elif choice == "2":

            mathematical_menu()

        elif choice == "3":

            random_menu()

        elif choice == "4":

            generate_uuid()

        elif choice == "5":

            file_menu()

        elif choice == "6":

            explore_module()

        elif choice == "7":

            print("\n==========================")

            print(
                "Thank you for using the "
                "Multi-Utility Toolkit!"
            )

            print("==========================")

            break

        else:

            print(
                "Invalid choice! "
                "Please try again."
            )


# PROGRAM START

if __name__ == "__main__":
    '''
    This starts our program.
If we run this file directly,
the main() function will run.
    '''

    main()