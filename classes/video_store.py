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