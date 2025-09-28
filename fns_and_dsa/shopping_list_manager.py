# fns_and_dsa/shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            item = input("Enter item to add: ").strip()
            if not item:
                print("No item entered. Nothing added.")
            else:
                shopping_list.append(item)
                print(f"'{item}' added to the shopping list.")
        elif choice == '2':
            if not shopping_list:
                print("Shopping list is empty. Nothing to remove.")
            else:
                item = input("Enter item to remove: ").strip()
                # Case-insensitive removal while preserving original item text
                found = False
                for i, existing in enumerate(shopping_list):
                    if existing.lower() == item.lower():
                        removed = shopping_list.pop(i)
                        print(f"'{removed}' removed from the shopping list.")
                        found = True
                        break
                if not found:
                    print(f"Item '{item}' not found in the shopping list.")
        elif choice == '3':
            if not shopping_list:
                print("Shopping list is empty.")
            else:
                print("Current shopping list:")
                for idx, itm in enumerate(shopping_list, start=1):
                    print(f"{idx}. {itm}")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

