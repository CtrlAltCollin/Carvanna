ids    = [1, 2, 3]
makes  = ["Toyota", "Honda", "Tesla"]
prices = [18000, 17000, 35000]

def show_inventory():
    for i in range(len(ids)):
        print(ids[i], makes[i], prices[i])

def search_by_budget(budget):
    for i in range(len(prices)):
        if prices[i] <= budget:
            print(ids[i], makes[i], prices[i])

def main():
    choice = ""

    while choice != "3":
        print("1 - Show cars")
        print("2 - Search by budget")
        print("3 - Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_inventory()

        elif choice == "2":
            budget = float(input("Budget: "))
            search_by_budget(budget)

    print("Goodbye!")

main()
