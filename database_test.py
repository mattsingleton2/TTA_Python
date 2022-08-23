import sqlite3

conn = sqlite3.connect('test.db')

with conn: 
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_persons(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn: 
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
        ('Bob','Smith','bsmith@gmail.com'))
    cursor.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
        ('Sarah','Jones','sjones@gmail.com'))
    cursor.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
        ('Sally','May','sallymay@gmail.com'))
    cursor.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?,?,?)", \
        ('Kevin','Bacon','gimmethebacon@gmail.com'))
    conn.commit()
conn.close()

conn = sqlite3.connect('test.db')

with conn: 
    cursor = conn.cursor()
    cursor.execute("SELECT col_fname,col_lname,col_email FROM tbl_persons WHERE col_fname - 'Sarah'")
    selectedPerson = cursor.fetchall()
    for item in selectedPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0], item[1], item[2])
    print(msg)
conn.close()


#if __name__ == "__main__":
    