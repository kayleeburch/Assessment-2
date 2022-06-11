import csv

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
    
        
             