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
        result = []
        for customer in self.customers:
                result.append(customer.customer_id)
        if identifier in result:
            for customer in self.customers:
                if customer.customer_id == identifier:
                    print(f"== {customer.f_name} {customer.l_name} ==\n{customer.current_rentals.split('/')}")
        else:
            print("ID does not exists in database.")
    
    def add_customer(self, customer_id, account_type, f_name, l_name, current_rentals = ''):
        self.customers.append(Customer(customer_id, account_type, f_name, l_name, current_rentals))
        print(self.customers)
  
        
    def renting_video(self, identifier, title):
        result = []
        type_of_account = ''
        curr_rentals = 0
        for customer in self.customers:
            result.append(customer.customer_id)
        if identifier in result:
            for customer in self.customers:
                if customer.customer_id == identifier:
                    type_of_account = customer.account_type
                    curr_rentals = len(customer.current_rentals.split('/'))
                    if curr_rentals == ['']:
                        curr_rentals = 0
            print(curr_rentals, type_of_account, len([]))
            checking_rental_ability = Customer.able_to_rent(type_of_account, curr_rentals, title)
            print(checking_rental_ability) 
        else:
            print("ID does not exists in database.")