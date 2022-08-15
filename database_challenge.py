import sqlite3

# Creating our connection variable. 
# No need to type sqlite3.connect('challenge.db') every
# single time we want to work with it.
conn = sqlite3.connect('challenge.db')

# As long as the connection's true...
with conn:
    # Our cursor variable is required to execute on our db.
    cursor = conn.cursor()
    # Now let's tell that cursor what to do. 
    # Create a table if it doesn't already exist. 
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        filename TEXT NOT NULL )")
    # Let's commit that transaction
    conn.commit()
# And we close the connection to ensure we give that memory back.
conn.close()

# Setting up the file list per the challenge requirements.
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdg', 'myPhoto.jpg')

# Let's look through fileList for qualifying txt files and add them to the table.
for file in fileList:
    if '.txt' in file:
        conn = sqlite3.connect('challenge.db')
        with conn:
            cursor = conn.cursor()
            # Use the cursor to execute our table addition.
            cursor.execute("INSERT INTO tbl_files (filename) VALUES (?)", (file,))
            # And log the added files to the console.
            print("{} was added to the challenge database.".format(file))
        conn.close()