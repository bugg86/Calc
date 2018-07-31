loops = True


def loop(): # defines the whole program as a function
    first_number = input("Please enter your first number: ")    # stores the first number as a variable

    def add():  # the addition function
        second_number = input("Please enter your second number: ")      # stores the second number as a variable
        result = int(first_number) + int(second_number)     # calculates the result
        print(result)   # prints the result

    def subtract():     # the subtraction function
        second_number = input("Please enter your second number: ")
        result = int(first_number) - int(second_number)
        print(result)

    def divide():   # the division function
        second_number = input("Please enter your second number: ")
        result = int(first_number) / int(second_number)
        print(result)

    def multiply(): # the multiply function
        second_number = input("Please enter your second number: ")
        result = int(first_number) * int(second_number)
        print(result)

    operation = input("Do you want to add, subtract, divide, or multiply your numbers?  ")
    """These if and elif statements determines which operation to do"""
    if operation == 'add':
        add()
    elif operation == 'subtract':
        subtract()
    elif operation == 'divide':
        divide()
    elif operation == 'multiply':
        multiply()
    else:
        print("That is not a valid operation.")


while loops:    # loops the function
    loop()