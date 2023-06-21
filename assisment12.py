# Fruit Manager module

fruit_stock = {}

def add_fruit(name, quantity):
    if name in fruit_stock:
        fruit_stock[name] += quantity
    else:
        fruit_stock[name] = quantity
    print(f"{quantity} {name}(s) added to the stock.")

def view_fruit_stock():
    if fruit_stock:
        print("Fruit Stock:")
        for fruit, quantity in fruit_stock.items():
            print(f"{fruit}: {quantity}")
    else:
        print("Fruit stock is empty.")

def update_fruit_stock(name, quantity):
    if name in fruit_stock:
        fruit_stock[name] = quantity
        print(f"{name} stock updated to {quantity}.")
    else:
        print(f"{name} does not exist in the fruit stock.")
        # Customer module

import fruit_manager

def buy_fruit(name, quantity):
    if name in fruit_manager.fruit_stock:
        if fruit_manager.fruit_stock[name] >= quantity:
            fruit_manager.fruit_stock[name] -= quantity
            print(f"Successfully purchased {quantity} {name}(s).")
        else:
            print(f"Insufficient {name} stock.")
    else:
        print(f"{name} does not exist in the fruit stock.")
        # Main module

import fruit_manager
import customer

def display_menu():
    print("Fruit Store")
    print("1. Add fruit stock")
    print("2. View fruit stock")
    print("3. Update fruit stock")
    print("4. Buy fruit")
    print("5. Exit")

def handle_choice(choice):
    if choice == 1:
        name = input("Enter fruit name: ")
        quantity = int(input("Enter quantity: "))
        fruit_manager.add_fruit(name, quantity)
    elif choice == 2:
        fruit_manager.view_fruit_stock()
    elif choice == 3:
        name = input("Enter fruit name: ")
        quantity = int(input("Enter quantity: "))
        fruit_manager.update_fruit_stock(name, quantity)
    elif choice == 4:
        name = input("Enter fruit name: ")
        quantity = int(input("Enter quantity: "))
        customer.buy_fruit(name, quantity)
    elif choice == 5:
        exit()
    else:
        print("Invalid choice. Please try again.")

def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        handle_choice(choice)

if _name_ == "_main_":
    main()
