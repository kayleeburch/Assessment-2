from classes.inventory import Inventory
from classes.customer import Customer

class Video_Store():
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory.total_inventory()
        self.customers = Customer.customer_info()
        
    
    def view_inventory(self):
        for video in self.inventory:
            print(f"=== {video.title} ===\nID: {video.video_id}\nRating: {video.rating}\nRelease Date: {video.release_date}\nTotal Copies: {video.copies}")
            
            
    def view_rentals(self, identifier):
        if self.id_exists(identifier) == False:
            print("ID does not exists in database.")
            return
        else:
            for customer in self.customers:
                if customer.customer_id == identifier:
                    print(f"== {customer.f_name} {customer.l_name} ==\n{customer.current_rentals.split('/')}")
                    
    
    def add_customer(self, customer_id, account_type, f_name, l_name, current_rentals = ''):
        if self.id_exists(customer_id) == True:
            print("ID already exists in database.")
            return
        elif account_type not in ['sx', 'px', 'sf', 'pf']:
            print('Not a valid account type, please try again.')
            return
        else:
            self.customers.append(Customer(customer_id, account_type, f_name, l_name, current_rentals))
            return
  
        
    def renting_video(self, identifier, title):
        type_of_account = ''
        curr_rentals = 0
        if self.id_exists(identifier) == False:
            print("ID does not exists in database.")
            return
        elif Inventory.title_exists(title) == False:
            print('Title does not exists in database.')
            return
        else:
            for customer in self.customers:
                if customer.customer_id == identifier:
                    type_of_account = customer.account_type
                    curr_rentals = len(customer.current_rentals.split('/'))
                    if customer.current_rentals.split('/') == ['']:
                        curr_rentals = 0
                    print(curr_rentals, type_of_account)
                    checking_rental_ability = Customer.able_to_rent(type_of_account, curr_rentals, title)
                    if checking_rental_ability == True:
                        if curr_rentals == 0:
                            customer.current_rentals = customer.current_rentals + f"{title}"
                            self.updating_inventory(title, -1)
                        else:
                            customer.current_rentals = customer.current_rentals + f"/{title}"
                            self.updating_inventory(title, -1)
                    else:
                        return checking_rental_ability
        
            
    def returning_video(self, identifier, title):
        if self.id_exists(identifier) == False:
            print("ID does not exists in database.")
            return
        elif Inventory.title_exists(title) == False:
            print('Title does not exists in database.')
            return
        else:
            for customer in self.customers:
                if customer.customer_id == identifier:
                    customer_arr = customer.current_rentals.split('/')
                    # print(customer.current_rentals, customer_arr)
                    if title in customer_arr:
                        customer_arr.remove(title)
                        new_str = '/'.join(customer_arr)
                        customer.current_rentals = new_str
                        self.updating_inventory(title, 1)
                    else:
                        print('Customer does not have this movie rented.')
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
                print(int(movie.copies), amount, adding_copy)
                movie.copies = str(adding_copy)