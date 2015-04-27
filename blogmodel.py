
'''

Blog Model

Create a class to interface with sqlite3.  This type of object is typically called a Model.

The table in sqlite3 will have two columns: post_name and post_text

Discuss with your neighbour on how to solve this challenge.

To connect Python to SQL, reference the following:
http://www.pythoncentral.io/introduction-to-sqlite-in-python/

Your model should be able to:

1) Open a sqlite3 db connection
2) Close the connection
3) Create a new table with the correct fields
4) Perform CRUD actions on the database table

C - Create
R - Read
U - Update
D - Destroy

'''

import sqlite3


class BlogModel():
    def __init__(self,db_file):
        self.db_file = db_file

        self.post_name = None
        self.post_text = None

    def open(self):
        "open sqlite3 db connection"
        self.db = sqlite3.connect(self.db_file)

    def close(self):
        "close the connection to sqlite3"
        self.db_file.close()

    def create_table(self):
        #create the table
        cursor = self.db.cursor()
        cursor.execute('''CREATE TABLE blogdb(id INTEGER PRIMARY KEY, post_name TEXT,
                       post_text TEXT)
            ''')
        self.db.commit()

    def create(self, post_name, post_text):
        #create a new row with data that you pass in
        cursor = self.db.cursor()
        cursor.execute('''INSERT INTO blogdb(post_name, post_text)
                  VALUES(?,?)''', (post_name, post_text))
        self.db.commit()
        print 'Post created'

    def read(self,id):
        # "search for id, and return post_name and post_text as a string"
        cursor = self.db.cursor()
        cursor.execute('''SELECT post_name, post_text FROM blogdb WHERE id=?''', (id,))
        post = cursor.fetchone()
        for i in post:
            print i

    def update(self, id, post_name, post_text):
        # "search for id, and set a new post_name and post_text"
        cursor = self.db.cursor()
        cursor.execute('''UPDATE blogdb SET post_name = ?, post_text = ? WHERE id = ? ''', (post_name, post_text, id))
        self.db.commit()

    def destroy(self,id):
        #"search for id, and delete that row"
        cursor = self.db.cursor()
        cursor.execute('''DELETE FROM blogdb WHERE id = ? ''', (id,))
        self.db.commit()


test_db = BlogModel("first_db.db")
test_db.open()
test_db.create("First Post!", "All the words!")
test_db.read("1")
test_db.update("1", "Better first post", "still more words!")
test_db.read("1")
