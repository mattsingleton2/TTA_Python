import os
import datetime

# Setting absolute file path
fPath = os.path.abspath('C:\\Users\\matts\\Desktop\\FilePractice\\')

# os.listdir(fPath) will iterate through all the files and list them, the 
# for loop will actually stash those into a list for me to iterate over.
def createFileList():
    # initialize the list
    fileList = []
    # set up for loop iteration to grab the files
    for file in os.listdir(fPath):
        # We actually need two pieces here. The absolute directory and file type
        # as well as the last time the piece was modified. Let's keep our
        # code clean by saving those in different variables...
        # First up is our file name and path.
        filePath = os.path.abspath(os.path.join(fPath,file))
        
        # Next up is the last modification time/date.
        fileModEpochTime = os.path.getmtime(filePath)

        # Let's make this more readable
        fileReadableTime = datetime.datetime.fromtimestamp(fileModEpochTime)
        
        
        # Now, we should only print the .txt files to the console with their last modified timestamp.
        # so we should use an if and check the suffix?
        if '.txt' in filePath:
            print("\nThe text file at \n{}\nwas last modified on {}.\n".format(filePath, fileReadableTime))
        

    
if __name__ == "__main__":
    createFileList()
    