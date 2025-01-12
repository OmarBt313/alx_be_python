# shopping_list =[]




# while True :

    
    
#     i = int(input('to display all items in your chopping list click 1\nto add an item click 2\nto remove an item click 3\nto exit click 0\n'))

#     if i == 1:
#         print(shopping_list)
    
#     elif i == 2:
#         shopping_list.append(input('type you item and click enter to add it:\n'))

#     elif i == 3:
        # remove = input('what item would you like to remove:\n')

        # for x in range(shopping_list):
        #     if remove == shopping_list[x]:
        #         shopping_list.remove(x)

#     else:
#         break





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
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            shopping_list.append(input('Enter the item to add:1\n'))
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove = input('what item would you like to remove:\n')

            for x in range(len(shopping_list)):
                if remove == shopping_list[x]:
                    shopping_list.remove(shopping_list[x])
            pass
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()