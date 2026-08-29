def create_file():
    '''
    This function creates a new text file.

    The user enters the file name.
    If the file already exists, an error message is displayed.
    '''

    filename = input("Enter file name: ")

    try:
        with open(filename, "x") as file:
            pass

        print("File created successfully!")

    except FileExistsError:
        print("File already exists!")


def write_file():
    '''
    This function writes data into a file.

    The 'w' mode is used for writing.
    If the file does not exist, Python creates it.
    '''

    filename = input("Enter file name: ")
    data = input("Enter data to write: ")

    try:
        with open(filename, "w") as file:
            file.write(data)

        print("Data written successfully!")

    except Exception as e:
        print("Error:", e)


def read_file():
    '''
    This function reads data from a file.

    The 'r' mode is used for reading.
    '''

    filename = input("Enter file name: ")

    try:
        with open(filename, "r") as file:
            data = file.read()

        print("\nFile Content:")
        print(data)

    except FileNotFoundError:
        print("File not found!")


def append_file():
    '''
    This function adds new data at the end of a file.

    The 'a' mode is used for appending data.
    '''

    filename = input("Enter file name: ")
    data = input("Enter data to append: ")

    try:
        with open(filename, "a") as file:
            file.write("\n" + data)

        print("Data appended successfully!")

    except Exception as e:
        print("Error:", e)