def num_check(question):
    error = "please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine Goes Here...

keep_going = ""
while keep_going == "":
    # Get width and height
    width = num_check("Width: ")
    length = num_check("Length: ")
    cost = num_check("Cost: ")

    # Calculate perimeter and price for the fence
    perimeter = 2 * (width + length)
    price = (perimeter * cost)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price: ${price:.2f}")

    # Ask user if they want to keep going
    keep_going = input(" Press enter to keep going or any key to quit")
    print()

print(" Thank you for using the calculator")
