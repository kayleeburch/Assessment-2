import csv

class Inventory():
    def __init__(self, video_id, title, rating, release_date, copies):
        self.video_id = video_id
        self.title = title
        self.rating = rating
        self.release_date = release_date
        self.copies = copies
    
    def total_inventory():
        video_objects = []
        with open('data/inventory.csv', newline='') as f:
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