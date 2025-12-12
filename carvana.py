def show_faq():
    # Opens and displays the FAQ file
    faq_file = open('faq.txt', 'r')
    faq_contents = faq_file.read()
    faq_file.close()
    print("\n" + faq_contents + "\n")


def is_number(value):
    # Checks if input can be converted into a number
    try:
        int(value)
        return True
    except:
        return False


def equals_faq(text):
    # Checks if user typed FAQ in any letter combination
    return (
        text == "FAQ" or text == "faq" or text == "Faq" or
        text == "fAQ" or text == "faQ" or text == "FAq" or text == "fAq"
    )


def get_input_with_faq(prompt):
    # Gets user input and allows FAQ access
    user_input = input(prompt)

    while equals_faq(user_input):
        show_faq()
        user_input = input(prompt)

    return user_input


def extract_price(spec_line):
    # Extracts the price from the specs line manually
    dollar_index = -1
    index = 0

    # Find the dollar sign
    while index < len(spec_line):
        if spec_line[index] == '$':
            dollar_index = index
            break
        index += 1

    price_str = ""
    i = dollar_index + 1

    # Collect digits after the dollar sign
    while i < len(spec_line):
        ch = spec_line[i]

        if ch >= '0' and ch <= '9':
            price_str = price_str + ch
        elif ch == ',':
            pass
        else:
            break

        i += 1

    # Convert extracted price to integer
    try:
        return int(price_str)
    except:
        return 0


def main():
    print("===================================")
    print("        WELCOME TO CARVANA         ")
    print("===================================\n")

    print("At any point, type FAQ for help.\n")

    open_carvana = get_input_with_faq("Would you like to open Carvana? (y/n): ")

    if open_carvana != 'y':
        print("Okay, goodbye!")
        return

    print("\nWelcome to Carvana!\n")
    print("Here is our catalog:\n")

    # Read catalog file
    catalog_file = open('catalog.txt', 'r')
    catalog_lines = catalog_file.readlines()
    catalog_file.close()

    # Display catalog with numbering
    number = 1
    for line in catalog_lines:
        clean = line.strip()
        if clean != "":
            print(str(number) + ". " + clean)
            number += 1

    print()

    # Vehicle selection
    user_input = get_input_with_faq("Which number car would you like to view? ")

    while not is_number(user_input):
        print("Please enter a valid number.")
        user_input = get_input_with_faq("Which number car would you like to view? ")

    choice = int(user_input)

    # Read specs file
    specs_file = open('specs.txt', 'r')
    specs_lines = specs_file.readlines()
    specs_file.close()

    if choice < 1 or choice > len(specs_lines):
        print("\nThat number is not in the catalog.")
        back = input("Would you like to return to the catalog? (y/n): ")

        if back == 'y':
            main()
        return

    chosen_specs = specs_lines[choice - 1].strip()

    print("\nHere are the details for that car:\n")
    print(chosen_specs)

    proceed = input("Would you like to proceed with purchasing this car? (y/n): ")

    if proceed != 'y':
        print("Thank you for visiting Carvana!")
        return

    print("\nGreat! Let’s begin the purchasing process.\n")

    # TRADE-IN
    print("\n--- TRADE-IN INFORMATION ---\n")

    trade = input("Do you have a trade-in vehicle? (y/n): ")
    trade_value = 0

    if trade == 'y':
        year = input("Enter the year of your vehicle: ")
        while not is_number(year):
            print("Please enter a valid year.")
            year = input("Enter the year of your vehicle: ")

        make = input("Enter the make of your vehicle: ")
        model = input("Enter the model of your vehicle: ")

        import random
        trade_value = random.randint(2000, 15000)

        print("\nTrade-in Offer: $", trade_value, sep='')

    # INCOME / DOWN PAYMENT
    print("\n--- INCOME & DOWN PAYMENT ---\n")

    income_input = input("Enter your yearly income: ")
    while not is_number(income_input):
        print("Please enter a valid number.")
        income_input = input("Enter your yearly income: ")

    down_input = input("Enter your down payment amount: ")
    while not is_number(down_input):
        print("Please enter a valid number.")
        down_input = input("Enter your down payment amount: ")

    # SHIPPING
    print("\n--- SHIPPING OPTIONS ---\n")

    shipping = input("Would you like shipping? (y/n): ")
    shipping_cost = 0
    shipping_address = ""

    if shipping == 'y':
        shipping_cost = 500

        print("\nPlease enter your shipping address.")
        street = input("Street Address: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("ZIP Code: ")

        shipping_address = street + ", " + city + ", " + state + " " + zip_code

    # PRICE & TAX
    price = extract_price(chosen_specs)
    tax_amount = int(price * 0.08875)

    # PAYMENT OPTIONS
    print("\n--- PAYMENT OPTIONS ---\n")
    print("1. Cash")
    print("2. Self-financing (pre-approved loan)")
    print("3. Finance with Carvana")

    payment_choice = input("Enter 1, 2, or 3: ")

    while payment_choice not in ['1', '2', '3']:
        print("Please enter 1, 2, or 3.")
        payment_choice = input("Enter 1, 2, or 3: ")

    financing_type = ""
    monthly_payment = 0
    finance_months = 0
    interest_rate = 0

    # CASH
    if payment_choice == '1':
        financing_type = "Cash Purchase"
        total_due = price + tax_amount - trade_value + shipping_cost

    # SELF-FINANCING
    elif payment_choice == '2':
        financing_type = "Self-Financing"

        months_input = input("How many months is your loan? ")
        while not is_number(months_input):
            print("Please enter a valid number.")
            months_input = input("How many months is your loan? ")

        finance_months = int(months_input)
        total_due = price + tax_amount - trade_value + shipping_cost
        monthly_payment = total_due // finance_months

    # CARVANA FINANCING
    elif payment_choice == '3':
        financing_type = "Carvana Financing"
        interest_rate = 0.06

        months_input = input("How many months do you want to finance for? ")
        while not is_number(months_input):
            print("Please enter a valid number.")
            months_input = input("How many months do you want to finance for? ")

        finance_months = int(months_input)
        total_due = price + tax_amount - trade_value + shipping_cost
        interest_amount = int(total_due * interest_rate)
        total_due = total_due + interest_amount
        monthly_payment = total_due // finance_months

    # PURCHASE SUMMARY
    print("\n--- PURCHASE SUMMARY ---\n")
    print("Base Price: $", price, sep='')
    print("Sales Tax: $", tax_amount, sep='')
    print("Trade-in: -$", trade_value, sep='')
    print("Shipping: $", shipping_cost, sep='')
    print("TOTAL DUE: $", total_due, sep='')

    final_buy = input("Would you like to complete your purchase? (y/n): ")

    if final_buy == 'y':
        print("\n========== FINAL RECEIPT ==========\n")
        print("TOTAL PAID: $", total_due, sep='')
        print("Payment Method:", financing_type)

        if shipping == 'y':
            print("Shipping Address:")
            print(shipping_address)
            print("Estimated Delivery: 7 days")
        else:
            print("Pickup Location:")
            print("2 North Ave, Garden City, NY 11530")

        print("\nThank you for choosing Carvana!")
        return

    back = input("Would you like to return to the catalog? (y/n): ")

    if back == 'y':
        main()
    else:
        print("Thank you for visiting Carvana!")


# Run the program
main()
