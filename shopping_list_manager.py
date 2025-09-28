#!/usr/bin/python3
"""
A simple shopping list manager using a Python list.
"""

def display_menu():
    """Prints the main menu for the user."""
    # CORRECTED LINE: Removed the '\n' from the start of this string
    print("Shopping List Manager") 
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to run the shopping list manager."""
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' was added to the list.")

        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' was removed from the list.")
            else:
                print(f"'{item}' not found in the list.")

        elif choice == '3':
            # Display the shopping list
            if not shopping_list:
                print("The shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("------------------------")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
