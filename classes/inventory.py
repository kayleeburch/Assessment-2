import csv
from re import T

class Inventory():
    def __init__(self, video_id, title, rating, release_date, copies):
        self.video_id = video_id
        self.title = title
        self.rating = rating
        self.release_date = release_date
        self.copies = copies
        
    
    def total_inventory(): #returns inventory objects in list from csv file
        video_objects = []
        with open('data/inventory.csv', newline='') as f:
            csv_reader = csv.reader(f, delimiter='\n')
            next(f)
            for row in csv_reader:
                items = row[0].split(',')
                inventory_info = {'video_id': items[0], 'title': items[1], 'rating':items[2], 'release_date':items[3], 'copies': items[4]}
                video_objects.append(Inventory(**inventory_info))
        f.close()
        return video_objects
    
    def available_inventory(title, objects): #is called to check inventory copy amount
        rating = ''
        number_of_copies = 0
        enough_copies = True
        inventory_objects = objects 
        if Inventory.title_exists(title) != True: #checking to see if title exists
            print("Title does not exist in inventory, please try again.")
            return
        else:
            for movie in inventory_objects:
                if movie.title == title:
                    rating = movie.rating
                    number_of_copies = movie.copies
            if number_of_copies == '0': #if number_of_copies == 0 return False, else return the rating of the movie with title passed in
                enough_copies = False
                return enough_copies
            else:
                return rating
            
    def title_exists(t): #returns true of false if movie title
        result = []
        inventory_objects = Inventory.total_inventory() #calls the total_inventory() method in Inventory
        for movie in inventory_objects: #appends the movie titles in inventory objects and tests to see if title passed as param (t), exists.
            result.append(movie.title)   
        if t in result:
            return True
        else:
            return False
        
   
        