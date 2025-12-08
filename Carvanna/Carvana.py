def show_faq():
    # Opens and displays the FAQ file
    faq_file = open('faq.txt', 'r')
    faq_contents = faq_file.read()
    faq_file.close()
    print("\n" + faq_contents + "\n")


def get_input_with_faq(prompt):
    # Asks for input, shows FAQ when user types FAQ
    user_input = input(prompt)

    while user_input.upper() == "FAQ":
        show_faq()
        user_input = input(prompt)

    return user_input


def main():
    print("===================================")
    print("        WELCOME TO CARVANA         ")
    print("===================================\n")

    print("At any point in time, if you would like to open the FAQ, please type FAQ.\n")

    open_carvana = get_input_with_faq('Would you like to open Carvana? (y/n): ')

    if open_carvana != 'y':
        print('Okay, goodbye!')
        return

    print("\nWelcome to Carvana, where one man's trash is another man's treasure!\n")
    print('Here is our catalog:\n')

    # Read catalog
    catalog_file = open('catalog.txt', 'r')
    catalog_lines = catalog_file.readlines()
    catalog_file.close()

    # Print catalog with numbers
    number = 1
    for line in catalog_lines:
        line = line.strip()
        if line != "":
            print(str(number) + ". " + line)
            number += 1

    print()

    # Tell the user to pick from the list
    print("Please choose a number from the list above.\n")

    # Ask which car #
    user_input = get_input_with_faq('Which number car would you like to view? ')

    while not user_input.isdigit():
        print("Please enter a number.\n")
        user_input = get_input_with_faq('Which number car would you like to view? ')

    choice = int(user_input)

    # Read specs
    specs_file = open('specs.txt', 'r')
    specs_lines = specs_file.readlines()
    specs_file.close()

    # Validate car choice
    if choice < 1 or choice > len(specs_lines):
        print("\nThat number is not in the catalog. Please restart the program.\n")
        return

    # Retrieve selected car specs
    chosen_specs = specs_lines[choice - 1].strip()

    print("\nHere are the details for that car:\n")
    print(chosen_specs)

    proceed = input('Would you like to proceed with purchasing this car? (y/n): ')

    if proceed == 'y':
        print("\nGreat! Let’s begin the purchasing process.\n")

        # ===================================================
        # TRADE-IN
        # ===================================================
        # Display section header for trade-in information
        print("\n--- TRADE-IN INFORMATION ---\n")

        trade = input('Do you have a trade-in vehicle? (y/n): ')
        trade_value = 0

        if trade == 'y':
            year = input('Enter the year of your vehicle: ')
            while not year.isdigit():
                print("Please enter a valid year.")
                year = input('Enter the year of your vehicle: ')

            make = input('Enter the make of your vehicle: ')
            model = input('Enter the model of your vehicle: ')

            import random
            trade_value = random.randint(2000, 15000)

            print("\nCarvana’s trade-in estimate for your:")
            print(year, make, model)
            print("Trade-in Offer: $", trade_value, "\n", sep='')

        # ===================================================
        # INCOME / DOWNPAYMENT PRECHECK
        # ===================================================
        # Display section header for income and down payment check
        print("\n--- INCOME & DOWNPAYMENT CHECK ---\n")

        income_input = input('Enter your yearly income: ')
        while not income_input.isdigit():
            print("Please enter a valid number.")
            income_input = input('Enter your yearly income: ')
        income = int(income_input)

        down_input = input('Enter your down payment amount: ')
        while not down_input.isdigit():
            print("Please enter a valid number.")
            down_input = input('Enter your down payment amount: ')
        down_payment = int(down_input)

        if income > 25000 and down_payment >= 500:
            approval = "Approved"
        else:
            approval = "Denied"

        # ===================================================
        # SHIPPING
        # ===================================================
        # Display section header for shipping options
        print("\n--- SHIPPING OPTIONS ---\n")

        shipping = input('Would you like shipping? (y/n): ')
        if shipping == 'y':
            shipping_cost = 500
        else:
            shipping_cost = 0

        # ===================================================
        # EXTRACT PRICE
        # ===================================================
        dollar_index = chosen_specs.find('$')
        price = 0
        if dollar_index != -1:
            price_str = chosen_specs[dollar_index+1:].replace(",", "")
            if price_str.isdigit():
                price = int(price_str)

        # ===================================================
        # PAYMENT OPTIONS
        # ===================================================
        # Display section header for payment method selection
        print("\n--- PAYMENT OPTIONS ---\n")

        print("How would you like to pay for the vehicle?")
        print("1. Cash")
        print("2. Self-financing (pre-approved loan)")
        print("3. Finance with Carvana")

        payment_choice = input("Enter 1, 2, or 3: ")

        while payment_choice not in ['1', '2', '3']:
            print("Please enter 1, 2, or 3.")
            payment_choice = input("Enter 1, 2, or 3: ")

        tax_rate = 0.08875
        tax_amount = int(price * tax_rate)

        financing_type = ""
        monthly_payment = 0
        finance_months = 0
        interest_rate = 0
        approved_amount = 0

        # ----------------------
        # CASH
        # ----------------------
        if payment_choice == '1':
            financing_type = "Cash Purchase"
            total_due = price + tax_amount - trade_value + shipping_cost

        # ----------------------
        # SELF-FINANCING
        # ----------------------
        elif payment_choice == '2':
            financing_type = "Self-Financing"
            interest_rate = 0

            approved_amount_input = input("How much are you pre-approved for? ")
            while not approved_amount_input.isdigit():
                print("Please enter a valid number.")
                approved_amount_input = input("How much are you pre-approved for? ")
            approved_amount = int(approved_amount_input)

            finance_months_input = input("How many months is your loan? ")
            while not finance_months_input.isdigit():
                print("Please enter a valid number.")
                finance_months_input = input("How many months is your loan? ")
            finance_months = int(finance_months_input)

            total_due = price + tax_amount - trade_value + shipping_cost
            monthly_payment = total_due // finance_months

        # ----------------------
        # CARVANA FINANCING
        # ----------------------
        elif payment_choice == '3':
            financing_type = "Carvana Financing"
            interest_rate = 0.06

            finance_months_input = input("How many months do you want to finance for? ")
            while not finance_months_input.isdigit():
                print("Please enter a valid number.")
                finance_months_input = input("How many months do you want to finance for? ")
            finance_months = int(finance_months_input)

            total_due = price + tax_amount - trade_value + shipping_cost
            interest_amount = int(total_due * interest_rate)
            total_due += interest_amount

            monthly_payment = total_due // finance_months

        # ===================================================
        # PURCHASE SUMMARY
        # ===================================================
        # Display section header for purchase summary and totals
        print("\n--- PURCHASE SUMMARY ---\n")

        print("Car Selected: " + chosen_specs)
        print("--------------------------------------")
        print("Base Price: $", price, sep='')
        print("NY Sales Tax (8.875%): $", tax_amount, sep='')
        print("Trade-in Value: -$", trade_value, sep='')
        print("Shipping Cost: $", shipping_cost, sep='')
        print("--------------------------------------")
        print("Payment Type:", financing_type)

        if financing_type != "Cash Purchase":
            print("Estimated Interest Rate:", interest_rate * 100, "%")
            print("Loan Term:", finance_months, "months")
            print("Estimated Monthly Payment: $", monthly_payment, sep='')

        print("--------------------------------------")
        print("TOTAL DUE: $", total_due, sep='')
        print("======================================\n")

        final_buy = input("Would you like to complete your purchase? (y/n): ")

        if final_buy == 'y':
            print("\n========== FINAL RECEIPT ==========\n")
            print("Thank you for purchasing your vehicle!")
            print("TOTAL PAID: $", total_due, sep='')
            print("Payment Method:", financing_type)

            if shipping == 'y':
                print("Your vehicle will arrive in 7 days.")
            else:
                print("You may pick up your vehicle at:")
                print("2 North Ave, Garden City, NY 11530")

            print("\nHave a wonderful day!\n")
            return

        go_back = input("Would you like to return to the catalog? (y/n): ")
        if go_back == 'y':
            print("\nReturning to catalog...\n")
            main()
            return
        else:
            print("Thank you for visiting Carvana!")
            return

    else:
        print('Thank you for visiting Carvana! Have a nice day!')
        return


# Run the program
main()
