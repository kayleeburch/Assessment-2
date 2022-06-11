import csv
from classes.inventory import Inventory

class Customer():
    def __init__(self, customer_id, account_type, f_name, l_name, current_rentals):
        self.customer_id = customer_id
        self.account_type = account_type
        self.f_name = f_name
        self.l_name = l_name
        self.current_rentals = current_rentals
        
    def customer_info():
        customer_objects = []
        with open('data/customers.csv', newline='') as f:
            csv_reader = csv.reader(f, delimiter='\n')
            next(f)
            for row in csv_reader:
                items = row[0].split(',')
                inventory_info = {'customer_id': items[0], 'account_type': items[1], 'f_name':items[2], 'l_name':items[3], 'current_rentals': items[4]}
                customer_objects.append(Customer(**inventory_info))
        f.close()
        return customer_objects
    
    def able_to_rent(type_of_account, rental_number, title):
        can_rent = False
        if type_of_account == 'sx':
            if rental_number == 1:
                return "Max one rental at a time. Please return rental first." #can I put name of rented movie here?
            elif rental_number == 0:
                if Inventory.available_inventory(title) != False: #check if avilable dvds for title of movie (Inventory)
                    can_rent = True
                    return can_rent
                else:
                    return can_rent
        elif type_of_account == 'px':
            if rental_number == 3:
                return "Max one rental at a time. Please return rental first."
            elif rental_number < 3:
                if Inventory.available_inventory(title) != False:
                    can_rent = True
                    return can_rent
                else:
                    return can_rent
        elif type_of_account == 'sf':
            if rental_number == 1:
                return "Max one rental at a time. Please return rental first."
            elif rental_number == 0:
                if Inventory.available_inventory(title) != False and Inventory.available_inventory(title) == 'R':
                    print("Unable to rent R rated movies with current account type")
                    return can_rent
                elif Inventory.available_inventory(title) == False:
                    return can_rent
                else:
                    can_rent = True
                    return can_rent
        elif type_of_account == 'pf':
            if rental_number == 3:
                return "Max one rental at a time. Please return rental first."
            elif rental_number < 3:
                if Inventory.available_inventory(title) != False and Inventory.available_inventory(title) == 'R':
                    print("Unable to rent R rated movies with current account type")
                    return can_rent
                elif Inventory.available_inventory(title) == False:
                    return can_rent
                else:
                    can_rent = True
                    return can_rent
            
        
        
             