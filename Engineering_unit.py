# Engineering Unit Converter
# CTE123 Python Mini Project

history = []


# Function to convert length
def length_converter(value, choice):
    if choice == 1:
        answer = value / 25.4
        return answer, "mm", "inches"
    else:
        answer = value * 25.4
        return answer, "inches", "mm"


# Function to convert temperature
def temperature_converter(value, choice):
    if choice == 1:
        answer = (value * 9 / 5) + 32
        return answer, "C", "F"
    else:
        answer = (value - 32) * 5 / 9
        return answer, "F", "C"


# Function to convert mass
def mass_converter(value, choice):
    if choice == 1:
        answer = value * 2.20462
        return answer, "kg", "lb"
    else:
        answer = value / 2.20462
        return answer, "lb", "kg"


# Function to convert speed
def speed_converter(value, choice):
    if choice == 1:
        answer = value / 3.6
        return answer, "km/h", "m/s"
    else:
        answer = value * 3.6
        return answer, "m/s", "km/h"


# Function to display the menu
def show_menu():
    print("\nENGINEERING UNIT CONVERTER")
    print("--------------------------")
    print("1. Length (mm and inches)")
    print("2. Temperature (C and F)")
    print("3. Mass (kg and lb)")
    print("4. Speed (km/h and m/s)")
    print("5. View history")
    print("6. Clear history")
    print("7. Exit")


# Function to perform conversion
def convert_units(option):

    print("\nChoose conversion direction:")
    print("1. First unit to second unit")
    print("2. Second unit to first unit")

    try:
        direction = int(input("Enter choice: "))

        if direction != 1 and direction != 2:
            print("Invalid direction!")
            return

        value = float(input("Enter value: "))

        if option == 1:
            result, unit1, unit2 = length_converter(value, direction)

        elif option == 2:
            result, unit1, unit2 = temperature_converter(value, direction)

        elif option == 3:
            result, unit1, unit2 = mass_converter(value, direction)

        elif option == 4:
            result, unit1, unit2 = speed_converter(value, direction)

        print("\nConversion Result:")
        print(f"{value:g} {unit1} = {result:.2f} {unit2}")

        # Save the result in history
        record = f"{value:g} {unit1} = {result:.2f} {unit2}"
        history.append(record)

    except ValueError:
        print("Invalid input! Please enter a number.")


# Function to display history
def show_history():

    print("\nCONVERSION HISTORY")

    if len(history) == 0:
        print("No conversions have been made yet.")

    else:
        for item in history:
            print(item)


# Function to clear history
def clear_history():

    if len(history) == 0:
        print("History is already empty.")

    else:
        history.clear()
        print("History cleared successfully.")


# Main program
while True:

    show_menu()

    try:
        choice = int(input("Select an option: "))

        if choice == 1 or choice == 2 or choice == 3 or choice == 4:
            convert_units(choice)

        elif choice == 5:
            show_history()

        elif choice == 6:
            clear_history()

        elif choice == 7:
            print("Thank you for using the converter!")
            break

        else:
            print("Invalid option! Choose between 1 and 7.")

    except ValueError:
        print("Please enter a valid menu number.")

    input("\nPress Enter to continue...")