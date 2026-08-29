import math


def factorial():
    '''
    This function calculates the factorial of a number.

    Example:
    5! = 5 x 4 x 3 x 2 x 1
    5! = 120
    '''

    number = int(input("Enter a number: "))

    if number < 0:

        print("Factorial is not possible for negative numbers.")

    else:

        result = 1

        for i in range(1, number + 1):

            result = result * i

        print("Factorial:", result)


def compound_interest():
    '''
    This function calculates compound interest.

    The user enters:
    Principal amount
    Rate of interest
    Time in years
    '''

    principal = float(
        input("Enter principal amount: ")
    )

    rate = float(
        input("Enter rate of interest (in %): ")
    )

    time = float(
        input("Enter time (in years): ")
    )

    amount = principal * (1 + rate / 100) ** time

    print(
        "Compound Interest:",
        round(amount, 2)
    )


def trigonometry():
    '''
    This function performs basic trigonometric calculations.

    It calculates:
    Sin
    Cos
    Tan
    '''

    angle = float(
        input("Enter angle in degrees: ")
    )

    radians = math.radians(angle)

    sine = math.sin(radians)
    cosine = math.cos(radians)
    tangent = math.tan(radians)

    print("Sin:", round(sine, 4))
    print("Cos:", round(cosine, 4))
    print("Tan:", round(tangent, 4))


def area_of_shapes():
    '''
    This function calculates the area of:
    1. Circle
    2. Rectangle
    3. Triangle
    '''

    print("\nArea of Geometric Shapes")

    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your choice: ")

    if choice == "1":

        radius = float(
            input("Enter radius: ")
        )

        area = math.pi * radius * radius

        print(
            "Area of Circle:",
            round(area, 2)
        )

    elif choice == "2":

        length = float(
            input("Enter length: ")
        )

        width = float(
            input("Enter width: ")
        )

        area = length * width

        print(
            "Area of Rectangle:",
            area
        )

    elif choice == "3":

        base = float(
            input("Enter base: ")
        )

        height = float(
            input("Enter height: ")
        )

        area = 0.5 * base * height

        print(
            "Area of Triangle:",
            area
        )

    else:

        print("Invalid choice!")