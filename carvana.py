def main():
    open_carvana = input('Would you like to open Carvana? (y/n): ')

    # If the answer is not "y", quit immediately
    if open_carvana != 'y':
        print('Okay, goodbye!')
        return

    # If we reach here, the answer was "y"
    print("Welcome to Carvana, where one man's trash is another man's treasure! \n")
    print('Here is our catalog:\n')

    catalog_file = open('catalog.txt', 'r')
    file_contents = catalog_file.readlines()
    catalog_file.close()

    number = 1

    for line in file_contents:
        line = line.strip()

        if line != "":
            print(str(number) + ". " + line)  
            number = number + 1

    print()
    choice = int(input('Which number car would you like to view? '))

    specs_file = open('specs.txt', 'r')
    specs_file_contents = specs_file.readlines()
    specs_file.close()

    index = choice - 1  
    chosen_specs = specs_file_contents[index].strip()

    print("Here are the details for that car:\n")
    print(chosen_specs)
            
# Call the main function
main()
