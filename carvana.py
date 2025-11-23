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

    while user_input == "FAQ":
        show_faq()
        user_input = input(prompt)

    return user_input

def main():
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

    # Ask which number car they want (FAQ allowed)
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
        print('Great here is the purchasing details of your specific car: ')
    else:
        print('Thank you for visiting Carvana! Have a nice day!')
    return
    
    
# Run the program
main()
