import tkinter as tk
from tkinter import * 
import tkinter.filedialog
import os
import shutil
import datetime
from datetime import *

#   Set up the window
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")
        
        #   Button to select files
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #   Paint it on the grid
        self.sourceDir_btn.grid(row=0, column=0, columnspan=2, padx=(20,10), pady=(30,0) )
        
        #   Create the entry field for that button
        self.source_dir = Entry(width=75)
        #   Paint it on the grid
        self.source_dir.grid(row=0, column=3, columnspan=2, padx=(20,10), pady=(30,0))
        
        #   Button to Select Destination
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #   Paint it
        self.destDir_btn.grid(row=1, column=0, columnspan=2, padx=(20,10), pady=(30,0))
        
        #   Create entry field for that button
        self.destination_dir = Entry(width=75)
        #   Paint it
        self.destination_dir.grid(row=1, column=3, columnspan=2, padx=(20,10), pady=(30,0))
        
        #   Create button to actually move the files from source to destination
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #   Paint it
        self.transfer_btn.grid(row=2, column=3, padx=(200,0), pady=(15,15))
        
        #   Exit button...
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #   Paint it
        self.exit_btn.grid(row=2, column=4, padx=(10,40), pady=(15,15))
    
    #   Create the function to handle selecting the source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #   Need to clear out the Entry text field
        self.source_dir.delete(0, END)
        #   And then insert the selected source
        self.source_dir.insert(0, selectSourceDir)
        
    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0,END)
        self.destination_dir.insert(0, selectDestDir)
        
        
    #   Function to move the files...
    def transferFiles(self):
        source = self.source_dir.get()
        destination = self.destination_dir.get()
        source_files = os.listdir(source)
        for file in source_files:
            #   Need to find out which files were created in the last 24 hours and only move those
            #   I should leave the ones older than 24 hours old.
            
            #   First, let's grab when the file was modified
            file_mod_epoch_time = os.path.getmtime(source + '/' + file)
            file_modTime = datetime.fromtimestamp(file_mod_epoch_time)
            print(file + ' was modified on {}'.format(file_modTime))
            
            #   Next we need to find out what time it currently is and subtract a day from it
            now = datetime.now()
            #   This establishes the delta, or the time difference for what we want to transfer.
            delta = timedelta(days=-1)
            #   This builds our boolean to use in our if statement below.
            #   Basically, we're checking to see if the changes to the file were more than a day ago.
            under24 = (file_modTime - now) >= delta
    
            #   Use our boolean to determine if the file should move. If true, move it, if not, explain that we didn't move it.
            if under24:
                #   shutil allows me to move those files from source to destination
                shutil.move(source + '/' + file, destination)
                print(file + ' was successfully transferred.')
            else:
                print(file + 'is older than 24 hours, so leaving that in source directory \n{}'.format(source))
            
    #   User needs to be able to exit this
    def exit_program(self):
        root.destroy()      
        
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()