import csv

class Video_Store():
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory.total_inventory()
    
    def view_inventory(self):
        for video in self.inventory:
            print(f"=== {video.title} ===\nID: {video.video_id}\nRating: {video.rating}\nRelease Date: {video.release_date}\nTotal Copies: {video.copies}")

    
class Inventory():
    def __init__(self, video_id, title, rating, release_date, copies):
        self.video_id = video_id
        self.title = title
        self.rating = rating
        self.release_date = release_date
        self.copies = copies
    
    def total_inventory():
        video_objects = []
        with open('data/store_inventory.csv', newline='') as f:
            csv_reader = csv.reader(f, delimiter='\n')
            next(f)
            for row in csv_reader:
                print(row)
                items = row[0].split(',')
                inventory_info = {'video_id': items[0], 'title': items[1], 'rating':items[2], 'release_date':items[3], 'copies': items[4]}
                print(items[0], items[4])
                video_objects.append(Inventory(**inventory_info))
        f.close()
        return video_objects
    
class Customer(Video_Store):
    def __init__(self):
        pass
    


def main():
    block_buster = Video_Store('Block Buster')
    while True:
        selection = input("\n== Welcome to Code Platoon Video ==\n1. View store video inventory\n2. View customer rented videos\n3. Add new customer\n4. Rent video\n5. Return video\n6. Exit\n")
        if selection == '1':
            block_buster.view_inventory()
        elif selection == '2':
            return
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