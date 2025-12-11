def show_faq():
    # Opens and displays the FAQ file
    faq_file = open('faq.txt', 'r')
    faq_contents = faq_file.read()
    faq_file.close()
    print("\n" + faq_contents + "\n")


def is_number(value):
    # Validates that the input is numeric (no .isdigit() allowed)
    try:
        int(value)
        return True
    except:
        return False


def equals_faq(text):
    # Manual version of text.upper() == "FAQ" (no .upper allowed)
    return text == "FAQ" or text == "faq" or text == "Faq" or text == "fAQ" or text == "faQ" or text == "FAq" or text == "fAq"


def get_input_with_faq(prompt):
    # Asks for input and checks for FAQ manually
    user_input = input(prompt)

    while equals_faq(user_input):
        show_faq()
        user_input = input(prompt)

    return user_input


def extract_price(spec_line):
    # Extracts price manually (no .find or .replace allowed)
    # Step 1: Find the '$'
    dollar_index = -1
    index = 0

    while index < len(spec_line):
        if spec_line[index] == '$':
            dollar_index = index
            break
        index += 1

    # Step 2: Collect digits after '$'
    price_str = ""
    i = dollar_index + 1

    while i < len(spec_line):
        ch = spec_line[i]
        # Accept digits and skip commas
        if (ch >= '0' and ch <= '9'):
            price_str = price_str + ch
        elif ch == ',':
            pass
        else:
            break
        i += 1

    # Convert to integer
    try:
        return int(price_str)
    except:
        return 0


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
        clean = line.strip()
        if clean != "":
            print(str(number) + ". " + clean)
            number += 1

    print()
    print("Please choose a number from the list above.\n")

    # Ask which car
    user_input = get_input_with_faq('Which number car would you like to view? ')

    while not is_number(user_input):
        print("Please enter a number.\n")
        user_input = get_input_with_faq('Which number car would you like to view? ')

    choice = int(user_input)

    # Read specs
    specs_file = open('specs.txt', 'r')
    specs_lines = specs_file.readlines()
    specs_file.close()

    # Validate
    if choice < 1 or choice > len(specs_lines):
        print("\nThat number is not in the catalog. Please restart the program.\n")
        return

    chosen_specs = specs_lines[choice - 1].strip()

    print("\nHere are the details for that car:\n")
    print(chosen_specs)

    proceed = input('Would you like to proceed with purchasing this car? (y/n): ')

    if proceed != 'y':
        print('Thank you for visiting Carvana! Have a nice day!')
        return

    print("\nGreat! Let’s begin the purchasing process.\n")

    # TRADE-IN
    print("\n--- TRADE-IN INFORMATION ---\n")

    trade = input('Do you have a trade-in vehicle? (y/n): ')
    trade_value = 0

    if trade == 'y':
        year = input('Enter the year of your vehicle: ')
        while not is_number(year):
            print("Please enter a valid year.")
            year = input('Enter the year of your vehicle: ')

        make = input('Enter the make of your vehicle: ')
        model = input('Enter the model of your vehicle: ')

        import random
        trade_value = random.randint(2000, 15000)

        print("\nCarvana’s trade-in estimate for your:")
        print(year, make, model)
        print("Trade-in Offer: $", trade_value, "\n", sep='')

    # INCOME / DOWN PAYMENT
    print("\n--- INCOME & DOWNPAYMENT CHECK ---\n")

    income_input = input('Enter your yearly income: ')
    while not is_number(income_input):
        print("Please enter a valid number.")
        income_input = input('Enter your yearly income: ')
    income = int(income_input)

    down_input = input('Enter your down payment amount: ')
    while not is_number(down_input):
        print("Please enter a valid number.")
        down_input = input('Enter your down payment amount: ')
    down_payment = int(down_input)

    if income > 25000 and down_payment >= 500:
        approval = "Approved"
    else:
        approval = "Denied"

    # SHIPPING
    print("\n--- SHIPPING OPTIONS ---\n")

    shipping = input('Would you like shipping? (y/n): ')
    if shipping == 'y':
        shipping_cost = 500
    else:
        shipping_cost = 0

    # PRICE EXTRACTION — no methods allowed
    price = extract_price(chosen_specs)

    # PAYMENT OPTIONS
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

    # CASH
    if payment_choice == '1':
        financing_type = "Cash Purchase"
        total_due = price + tax_amount - trade_value + shipping_cost

    # SELF-FINANCING
    elif payment_choice == '2':
        financing_type = "Self-Financing"
        interest_rate = 0

        approved_amount_input = input("How much are you pre-approved for? ")
        while not is_number(approved_amount_input):
            print("Please enter a valid number.")
            approved_amount_input = input("How much are you pre-approved for? ")
        approved_amount = int(approved_amount_input)

        finance_months_input = input("How many months is your loan? ")
        while not is_number(finance_months_input):
            print("Please enter a valid number.")
            finance_months_input = input("How many months is your loan? ")
        finance_months = int(finance_months_input)

        total_due = price + tax_amount - trade_value + shipping_cost
        monthly_payment = total_due // finance_months

    # CARVANA FINANCING
    elif payment_choice == '3':
        financing_type = "Carvana Financing"
        interest_rate = 0.06

        finance_months_input = input("How many months do you want to finance for? ")
        while not is_number(finance_months_input):
            print("Please enter a valid number.")
            finance_months_input = input("How many months do you want to finance for? ")
        finance_months = int(finance_months_input)

        total_due = price + tax_amount - trade_value + shipping_cost
        interest_amount = int(total_due * interest_rate)
        total_due = total_due + interest_amount

        monthly_payment = total_due // finance_months

    # PURCHASE SUMMARY
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


# Run program
main()
