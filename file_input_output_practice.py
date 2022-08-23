import os

def writeData(): 
    data = '\nHello World! This comment was added to the file with Python\'s I/O capabilities.'
    with open("README.md", 'a') as f:
        f.write(data)
        f.close()


def openFile():
    with open("README.md", 'r') as f:
        data = f.read()
        print(data)
        f.close()
        
        
if __name__ == "__main__":
    writeData()
    openFile()