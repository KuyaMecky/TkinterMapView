import tkintermapview
import os


# specify the region to load (New York City)
top_left_position = (40.801825, -74.161928)
bottom_right_position = (40.561993, -73.742846)
zoom_min = 0
zoom_max = 15

# specify path and name of the database
script_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(script_directory, "offline_tiles_nyc.db")

# create OfflineLoader instance
loader = tkintermapview.OfflineLoader(path=database_path)
loader.save_offline_tiles(top_left_position, bottom_right_position, zoom_min, zoom_max)

# You can call save_offline_tiles() multiple times and load multiple regions into the database

# print all regions that were loaded in the database
loader.print_loaded_sections()