import csv
from classes.inventory import Inventory

class Customer():
    def __init__(self, customer_id, account_type, f_name, l_name, current_rentals):
        self.customer_id = customer_id
        self.account_type = account_type
        self.f_name = f_name
        self.l_name = l_name
        self.current_rentals = current_rentals
        
    def customer_info(): #returns customer objects in list from csv file
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
    
    
    def able_to_rent(type_of_account, rental_number, title, objects): #is called when renting video method called within Inventory
        can_rent = False #sets boolean for if customer can rent or not
        if type_of_account == 'sx': #checks 'sx' account and number of rentals and sets max to 1
            if rental_number == 1:
                print("Max one rental at a time. Please return rental first.") 
                return can_rent
            elif rental_number == 0:
                if Inventory.available_inventory(title, objects) != False: #calls available_inventory method in Inventory to check available inventory, will return False if copies = 0
                    can_rent = True #set can_rent to true and return 
                    return can_rent
                else:
                    print('Not enough copies available in inventory.')
                    return can_rent
        elif type_of_account == 'px': #checks 'px' account and number of rentals and sets max to 3
            if rental_number == 3:
                print("Max 3 rentals at a time. Please return rental first.")
                return can_rent
            elif rental_number < 3:
                if Inventory.available_inventory(title, objects) != False:
                    can_rent = True
                    return can_rent
                else:
                    print('Not enough copies available in inventory.')
                    return can_rent
        elif type_of_account == 'sf': #checks 'sf' account and sets number of rentals to 1
            if rental_number == 1:
                print("Max one rental at a time. Please return rental first.")
                return can_rent
            elif rental_number == 0:
                if Inventory.available_inventory(title, objects) != False and Inventory.available_inventory(title, objects) == 'R': #checks if copies exist but movie is R rates
                    print("Unable to rent R rated movies with current account type.")
                    return can_rent
                elif Inventory.available_inventory(title, objects) == False: #checks if movie exists
                    print('Not enough copies available in inventory.')
                    return can_rent
                else:
                    can_rent = True #else return True
                    return can_rent
        elif type_of_account == 'pf': #checks 'pf' account and sets number of rentals to 3
            if rental_number == 3:
                print("Max one rental at a time. Please return rental first.")
                return can_rent
            elif rental_number < 3:
                if Inventory.available_inventory(title, objects) != False and Inventory.available_inventory(title, objects) == 'R': #checks if copies exist but movie is R rates
                    print("Unable to rent R rated movies with current account type.")
                    return can_rent
                elif Inventory.available_inventory(title, objects) == False: #checks if movie exists
                    print('Not enough copies available in inventory.')
                    return can_rent
                else:
                    can_rent = True #else return True
                    return can_rent
            
        
        
             