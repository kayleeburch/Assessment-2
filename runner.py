from classes.video_store import Video_Store
from classes.customer import Customer
from classes.inventory import Inventory
     

def main():
    block_buster = Video_Store('Block Buster')
    while True:
        selection = input("\n== Welcome to Code Platoon Video ==\n1. View store video inventory\n2. View customer rented videos {by id}\n3. Add new customer\n4. Rent video\n5. Return video\n6. Exit\n")
        if selection == '1':
            block_buster.view_inventory()
        elif selection == '2':
            search_id = input('Please enter customer ID: ')
            block_buster.view_rentals(search_id)
        elif selection == '3':
            return
        elif selection == '4':
            return
        elif selection == '5':
            return
        elif selection == '6':
            return
        else:
            print("Incorrect entry. Please select an option from the menu.")
            return

    
if __name__ == '__main__':
    main()