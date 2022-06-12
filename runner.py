from classes.video_store import Video_Store     

def main():
    block_buster = Video_Store('Block Buster') #creating instance of Video_Store class
    while True:
        selection = input("\n== Welcome to Code Platoon Video ==\n1. View store video inventory\n2. View customer rented videos {by id}\n3. Add new customer\n4. Rent video\n5. Return video\n6. Exit\n")
        if selection == '1':
            block_buster.view_inventory() #calls the view_inventory method in Video_Store
        elif selection == '2':
            search_id = input('Please enter customer ID: ')
            block_buster.view_rentals(search_id) #calls the view_rentals method in Video_Store, passing in a search ID as a parameter
        elif selection == '3':
            input_id = input('Please enter new customer ID: ')
            input_account_type = input('Please enter customer account type: ')
            input_first = input('Please enter customer first name: ')
            input_last = input('Please enter customer last name: ')
            block_buster.add_customer(input_id, input_account_type, input_first, input_last) #add customer takes in parameters for ID, account type, first and last name
        elif selection == '4':
            search_id_4 = input('Please enter customer ID: ')
            movie_title_input = input('Please enter movie title: ')
            block_buster.renting_video(search_id_4, movie_title_input) #calls the renting_video method in Video_Store and passes ID and title of movie
        elif selection == '5':
            search_id_5 = input('Please enter customer ID: ')
            title_input_5 = input('Please enter the title of movie being returned: ')
            block_buster.returning_video(search_id_5, title_input_5) #calls the returning_video method in Video_Store and passes ID and movie title
        elif selection == '6':
            return
        else:
            print("Incorrect entry. Please select an option from the menu.")
            return

    
if __name__ == '__main__':
    main()