from classes.inventory import Inventory

class Video_Store():
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory.total_inventory()
    
    def view_inventory(self):
        for video in self.inventory:
            print(f"=== {video.title} ===\nID: {video.video_id}\nRating: {video.rating}\nRelease Date: {video.release_date}\nTotal Copies: {video.copies}")