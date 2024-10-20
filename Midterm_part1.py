# Y Nhi Tran
# Midterm part 1
# This program write a menu-driven program for De Anza College Food Court.

# Constant variables, easy to change if the tax rate changes
TAX_RATE = 9 / 100


def show_menu():
    """
        This function show menu of De Anza College Food Court.
    """

    # Show the menu
    print("WELCOME TO DE ANZA COLLEGE FOOD COURT\n"
          "\n\t\tMenu\n"
          "1. De Anza Burger    $5.25\n"
          "2. Bacon Cheese      $5.75\n"
          "3. Mushroom Swiss    $5.95\n"
          "4. Western Burger    $5.95\n"
          "5. Don Cali Burger   $5.95\n"
          "6. Exit\n")


def get_inputs():
    """
        This function get inputs from user
    """

    # Get inputs and check the options and quantity are correct or not
    list = [0 for i in range(5)]
    command1 = "Enter option: "
    command2 = "Enter quantity: "

    ask = True
    while ask:
        try:
            option = int(input(command1))
            if option > 0 and option < 6:
                check = True
                while check:
                    try:
                        qty = int(input(command2))
                        if qty > 0:
                            list[option - 1] = list[option - 1] + qty
                            check = False
                        else:
                            print("Error! Please enter a number bigger than zero!")
                    except ValueError:
                        print("Please enter a number!")
            elif option == 6:
                ask = False
                break
            else:
                print("You have not entered from 1 to 6.\n"
                      "Please try again!")
                continue
        except ValueError:
            print("Please enter a number.")

    return option, list


def compute_bill(option, list):
    """
    This function compute the bill and print the option that user chose.
    """

    # Calculate the total before tax
    cost_menu = [5.25, 5.75, 5.95, 5.95, 5.95]
    total = 0
    tax = 0
    for i in range(5):
        total = total + list[i] * cost_menu[i]

    # Check if the user input nothing but option 6, then exit the program
    while total == 0:
        if option == 6:
            print("-" * 50)
            print("\t\t\t\tTHANK YOU!\n\t\t   HOPE TO SEE YOU AGAIN!")
            exit()

    # If the user order, then compute the bill
    while total != 0:
        command3 = "You are 1-Student or 2-Staff: "
        check = True
        while check:
            try:
                student = int(input(command3))
                if student == 1:
                    tax = 0
                    check = False
                elif student == 2:
                    tax = total * TAX_RATE
                    check = False
                else:
                    print("Error! This is not a correct option!")
            except ValueError:
                print("Error! This is not a numeric option!")

        # Print the order that user chose
        print()
        print(f'{"BILL":>20}')
        print(f'{"Items":>11}', f'{"Quantity":>18}', f'{"Cost":>11}')
        if list[0] != 0:
            print(f'{"1. De Anza Burger":<25}', list[0], f'{"$":>9}', f'{list[0] * 5.25:>5.2f}')
        if list[1] != 0:
            print(f'{"2. Bacon Cheese":<25}', list[1], f'{"$":>9}', f'{list[1] * 5.75:>5.2f}')
        if list[2] != 0:
            print(f'{"3. Mushroom Swiss":<25}', list[2], f'{"$":>9}', f'{list[2] * 5.95:>5.2f}')
        if list[3] != 0:
            print(f'{"4. Western Burger":<25}', list[3], f'{"$":>9}', f'{list[3] * 5.95:>5.2f}')
        if list[4] != 0:
            print(f'{"5. Don Cali Burger":<25}', list[4], f'{"$":>9}', f'{list[4] * 5.95:>5.2f}')

        total_bill = total + tax

        return total, tax, total_bill


def print_bill(total, tax, total_bill):
    """
        This function print the total before tax, tax amount,
        and the total after tax.
    """

    print("-" * 50)
    print(f'{"Total Before Tax":<35}', f'{"$":<1}' + f'{total :>6.2f}')
    print(f'{"Tax amount":<35}', f'{"$":<1}' + f'{tax :>6.2f}')
    print("-" * 50)
    print(f'{"Total After Tax":<35}', f'{"$":<1}' + f'{total_bill :>6.2f}')
    print("-" * 50)
    print("\t\t\t\tTHANK YOU!\n\t\t   HOPE TO SEE YOU AGAIN")


def main():
    """
    This function is to run main program.
    """

    show_menu()
    option, list = get_inputs()
    total, tax, total_bill = compute_bill(option, list)
    print_bill(total, tax, total_bill)


main()


# OUTPUT
# 1
# WELCOME TO DE ANZA COLLEGE FOOD COURT
#
# 		Menu
# 1. De Anza Burger    $5.25
# 2. Bacon Cheese      $5.75
# 3. Mushroom Swiss    $5.95
# 4. Western Burger    $5.95
# 5. Don Cali Burger   $5.95
# 6. Exit
#
# Enter option: a
# Please enter a number.
# Enter option: -9
# You have not entered from 1 to 6.
# Please try again!
# Enter option: 6
# --------------------------------------------------
# 				THANK YOU!
# 		   HOPE TO SEE YOU AGAIN!


#####################################################
# 2
# WELCOME TO DE ANZA COLLEGE FOOD COURT
#
# 		Menu
# 1. De Anza Burger    $5.25
# 2. Bacon Cheese      $5.75
# 3. Mushroom Swiss    $5.95
# 4. Western Burger    $5.95
# 5. Don Cali Burger   $5.95
# 6. Exit
#
# Enter option: a
# Please enter a number.
# Enter option: -9
# You have not entered from 1 to 6.
# Please try again!
# Enter option: 1
# Enter quantity: hello
# Please enter a number!
# Enter quantity: -9
# Error! Please enter a number bigger than zero!
# Enter quantity: 2
# Enter option: 3
# Enter quantity: 5
# Enter option: 6
# You are 1-Student or 2-Staff: a
# Error! This is not a numeric option!
# You are 1-Student or 2-Staff: -3
# Error! This is not a correct option!
# You are 1-Student or 2-Staff: 3
# Error! This is not a correct option!
# You are 1-Student or 2-Staff: 2
#
#                 BILL
#       Items           Quantity        Cost
# 1. De Anza Burger         2         $ 10.50
# 3. Mushroom Swiss         5         $ 29.75
# --------------------------------------------------
# Total Before Tax                    $ 40.25
# Tax amount                          $  3.62
# --------------------------------------------------
# Total After Tax                     $ 43.87
# --------------------------------------------------
# 				THANK YOU!
# 		   HOPE TO SEE YOU AGAIN

