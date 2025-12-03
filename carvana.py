def show_faq():
    # This function opens and displays the FAQ file
    faq_file = open('faq.txt', 'r')
    faq_contents = faq_file.read()
    faq_file.close()
    print("\n" + faq_contents + "\n")


def get_input_with_faq(prompt):
    # This function asks the user for input
    # If they type FAQ, it shows the FAQ and asks the same question again
    user_input = input(prompt)

    while user_input.upper() == "FAQ":
        show_faq()
        user_input = input(prompt)

    return user_input


def main():
    # ASCII banner
    print("===================================")
    print("        WELCOME TO CARVANA         ")
    print("===================================\n")

    print("At any point in time, if you would like to open the FAQ, please type FAQ.\n")

    # Ask the user if they want to open Carvana
    open_carvana = get_input_with_faq('Would you like to open Carvana? (y/n): ')

    if open_carvana != 'y':
        print('Okay, goodbye!')
        return

    print("\nWelcome to Carvana, where one man's trash is another man's treasure!\n")
    print('Here is our catalog:\n')

    # Open the catalog and read all lines
    catalog_file = open('catalog.txt', 'r')
    catalog_lines = catalog_file.readlines()
    catalog_file.close()

    # Print catalog with numbers
    number = 1
    for line in catalog_lines:
        line = line.strip()
        if line != "":
            print(str(number) + ". " + line)
            number = number + 1

    print()

    # Ask which number car they want 
    user_input = get_input_with_faq('Which number car would you like to view? ')

    # INPUT VALIDATION
    while not user_input.isdigit():
        print("Please enter a number.\n")
        user_input = get_input_with_faq('Which number car would you like to view? ')
  
    choice = int(user_input)

    # Open specs file and pick the chosen car's line
    specs_file = open('specs.txt', 'r')
    specs_lines = specs_file.readlines()
    specs_file.close()

    index = choice - 1
    chosen_specs = specs_lines[index].strip()

    print("\nHere are the details for that car:\n")
    print(chosen_specs)

    proceed = input('Would you like to proceed with purchasing this car? (y/n): ')

    if proceed == 'y':
        print('\nGreat! Let’s begin the purchasing process.\n')

        # Ask for trade-in
        trade = input('Do you have a trade-in vehicle? (y/n): ')
        trade_value = 0

        if trade == 'y':
            trade_input = input('Enter the trade-in value of your vehicle: ')
            while not trade_input.isdigit():
                print("Please enter a number.")
                trade_input = input('Enter the trade-in value of your vehicle: ')
            trade_value = int(trade_input)

        # Ask for pre-approval information
        income_input = input('Enter your yearly income: ')
        while not income_input.isdigit():
            print("Please enter a number.")
            income_input = input('Enter your yearly income: ')
        income = int(income_input)

        down_input = input('Enter your down payment amount: ')
        while not down_input.isdigit():
            print("Please enter a number.")
            down_input = input('Enter your down payment amount: ')
        down_payment = int(down_input)

        # Basic approval
        if income > 25000 and down_payment >= 500:
            approval = "Approved"
        else:
            approval = "Denied"

        # Shipping or pickup
        shipping = input('Would you like shipping? (y/n): ')
        if shipping == 'y':
            shipping_cost = 500
        else:
            shipping_cost = 0

        # PRINT RECEIPT 
        print("\n========== PURCHASE RECEIPT ==========\n")
        print("Car Selected: " + chosen_specs)
        print("Trade-in Value: $", trade_value, sep='')
        print("Down Payment: $", down_payment, sep='')
        print("Income: $", income, sep='')
        print("Loan Status:", approval)
        print("Shipping Cost: $", shipping_cost, sep='')
        print("\n======================================\n")

        # Offer to return to catalog
        go_back = input("Would you like to return to the catalog? (y/n): ")

        if go_back == 'y':
            print("\nReturning to catalog...\n")
            main()  # Restart program
            return
        else:
            print("Thank you for shopping with Carvana!")
            return

    else:
        print('Thank you for visiting Carvana! Have a nice day!')
        return


# Run the program
main()
