import sys
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "D:\apps\whitehatjunior\module 3\CLASS-102\C102_assets-main\C102_assets-main\extensions\Image_Files"


# Event Handler Class 
class FileEventHandler(FileSystemEventHandler):

    def on_created(self,event):
        print(f"Hey, {event.src_path} has been created!")

    def on_modified(self,event):
        print(f"Hey someone modified {event.src_path} ")  

    def on_moved(self,event):
        print(f"Oops! Someone deleted {event.src_path}")      

    def on_deleted(self,event):
        print(f"Oops! Someone deleted {event.src_path}!")    


# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()   

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()        