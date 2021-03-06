from classes.inventory import Inventory
from classes.customer import Customer

class Video_Store():
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory.total_inventory() #calls total_inventory method in Inventory to get Inventory objects
        self.customers = Customer.customer_info() #calls customer_info method in Customer to get Customer objects
        
    
    def view_inventory(self): #loops through inventory objects and prints the inventory information
        for video in self.inventory:
            print(f"=== {video.title} ===\nID: {video.video_id}\nRating: {video.rating}\nRelease Date: {video.release_date}\nTotal Copies: {video.copies}")
            
            
    def view_rentals(self, identifier): #takes in an id to check
        if self.id_exists(identifier) == False: #calls the id_exists method inside Video_Store to check if ID exists
            print("ID does not exists in database.")
            return
        else:
            for customer in self.customers:
                if customer.customer_id == identifier: #prints customer info and splits on the / for rentals 
                    print(f"== {customer.f_name} {customer.l_name} ==\n{customer.current_rentals.split('/')}")
                    
    
    def add_customer(self, customer_id, account_type, f_name, l_name, current_rentals = ''):
        if self.id_exists(customer_id) == True: #calls the id_exists method in Video_Store and checks if ID exists
            print("ID already exists in database.")
            return
        elif account_type not in ['sx', 'px', 'sf', 'pf']: #checks if account type is a valid account type
            print('Not a valid account type, please try again.')
            return
        else:
            self.customers.append(Customer(customer_id, account_type, f_name, l_name, current_rentals)) #appends the customer info to self.customers objects
            return
  
        
    def renting_video(self, identifier, title):
        type_of_account = '' #will hold account type
        curr_rentals = 0 #will hold number of rentals customer has
        if self.id_exists(identifier) == False: #checks if id exists
            print("ID does not exists in database.")
            return
        elif Inventory.title_exists(title) == False: #calls the method title_exists in the Inventory class to check if title is valid 
            print('Title does not exists in database.')
            return
        else:
            for customer in self.customers:
                if customer.customer_id == identifier:
                    type_of_account = customer.account_type #sets as account_type based on id
                    curr_rentals = len(customer.current_rentals.split('/')) #turns current rentals into array and sets as length of that array
                    if customer.current_rentals.split('/') == ['']: #if array is empty, set curr_rental to 0 vs 1
                        curr_rentals = 0
                    #calls the able_to_rent in Customer class and passes in account type, rental number, title, and the curr inventory objects
                    checking_rental_ability = Customer.able_to_rent(type_of_account, curr_rentals, title, self.inventory)
                    if checking_rental_ability == True: 
                        if curr_rentals == 0: #if return is true and rentals is 0
                            customer.current_rentals = customer.current_rentals + f"{title}" #update customer.current_rentals without the /
                            self.updating_inventory(title, -1) #method which adds -1 to total copies in inventory
                        else:
                            customer.current_rentals = customer.current_rentals + f"/{title}" #update customer.current_rentals with the /
                            self.updating_inventory(title, -1) #method which adds -1 to total copies in inventory
                    else:
                        return checking_rental_ability #if checking_rental_ability returns false, will return string
        
            
    def returning_video(self, identifier, title):
        if self.id_exists(identifier) == False: #checks ID 
            print("ID does not exists in database.")
            return
        elif Inventory.title_exists(title) == False: #check Title
            print('Title does not exists in database.')
            return
        else:
            for customer in self.customers:
                if customer.customer_id == identifier:
                    customer_arr = customer.current_rentals.split('/')
                    if title in customer_arr:
                        customer_arr.remove(title) #remove title from customer_arr 
                        new_str = '/'.join(customer_arr)
                        customer.current_rentals = new_str #set current_rentals to str without return title
                        self.updating_inventory(title, 1) #updating inventory copies +1
                    else:
                        print('Customer does not have this movie rented.') #if returning video that customer doesn't have rented
                        return
                        
    def id_exists(self, identifier):
        result = []
        for customer in self.customers:
            result.append(customer.customer_id)
        if identifier in result:
            return True
        else:
            return False
        
    def updating_inventory(self, t, amount):
        for movie in self.inventory:
            if movie.title == t:
                adding_copy = int(movie.copies) + amount
                movie.copies = str(adding_copy)
                
    