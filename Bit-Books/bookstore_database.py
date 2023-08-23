'''This file handles the bookstore database'''

# = = = = Imports = = = = #
import sqlite3
import os


class Bookstore_database():
    '''This Class handles the connection to the ebookstore database'''

    def __init__(self):
        """Constructor"""

        # Checks wether "user_db" exists, then create a default DB if not
        if self.ebookstore_db_exists() == False:
            # Creates directory if it does not exist
            if os.path.exists("eBookstore") != True:
                os.mkdir("eBookstore")
                
            # Creates ebookstore_db
            self.db = sqlite3.connect('eBookstore/ebookstore_db')
            self.cursor = self.db.cursor()

            # Creates books table
            self.create_Table()
            # Creates books
            self.insert_new_book_record(3001, "A Tale of Two Cities", "Charles Dickons", 30)
            self.insert_new_book_record(3002, "Harry Potter and the Philosophers Stone", "J.K Rowling", 40)
            self.insert_new_book_record(3003, "The Lion, the Witch and the Wardrobe", "C.S Lewis", 25)
            self.insert_new_book_record(3004, "The Lord of the Rings", "J.R.R Tolkien", 37)
            self.insert_new_book_record(3005, "Alice in Wonderland", "Lewis Carrol", 12)
            self.insert_new_book_record(3006, "The Programming behind Rockets", "Iwana Knowhow", 5)
            self.insert_new_book_record(3007, "The Art of War", "Sun Tzu", 65)
            self.insert_new_book_record(3008, "The Power of Now", "Eckhart Tolle", 23)
            self.insert_new_book_record(3009, "Pegasus", "L. Richard & S. Rigaud", 5)
            self.insert_new_book_record(3010, "Rocket Fuel", "Mistry Chem", 2)
            

        # Connects or create the user db
        self.db = sqlite3.connect('eBookstore/ebookstore_db')
        self.cursor = self.db.cursor()
    

    '''Contains all the methods for creating or deleting tables'''
    def create_Table(self):
        """Creates the default Users table"""
        try:
            self.cursor.execute('''
                                CREATE TABLE books(
                                Id INT(3),
                                Title VARCHAR(60),
                                Author VARCHAR(60),
                                QTY INT(4),
                                PRIMARY KEY (Id)
                                );''')
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
    

    def insert_new_book_record(self, id, title, author, qty):
        """Inserts new book details into book table"""
        try:
            self.cursor.execute('''INSERT INTO books
                                VALUES (?, ?, ?, ?)''', 
                                (id, title, author, qty))
            self.db.commit()
            print(f"The folowing record has been inserted: {id}, {title}, {author}, {qty}")
        except Exception as e:
            self.db.rollback()
            print(f"the following record was not inserted: {id},{title}{author},{qty}")
            raise e


    def ebookstore_db_exists(self):
        """returns a True value if 'ebookstore_db' file exists"""
        exists = False

        try:
            with open("eBookstore/ebookstore_db", "r") as file:
                exists = True
        except Exception:
            exists = False

        return exists
    

    def get_unassigned_id(self):
        """Finds an ID that has not yet been assigned"""
        # Starting point where to start searching for an available id
        id = 3001
        while True:
            
            try:
                self.cursor.execute('''SELECT * FROM books
                                    WHERE Id = ?;''', (id,))
                # Stores a record here that already matches with id
                record = self.cursor.fetchall()
                # If statement checking the length of record
                if len(record) > 0:
                    id += 1
                else:
                    break
            except Exception as e:
                raise e
            
        # returns id as available id
        return id


    def get_all_book_records(self):
        """Gets all the book records in books table"""
        try:
            # Executes query
            self.cursor.execute('''SELECT * FROM books''')
            books = self.cursor.fetchall()
            return books
        except Exception as e:
            raise e
        

    def search_by_title(self, title):
        """Search the title field in books for a specific word"""
        try:
            # Executes query
            self.cursor.execute(f'''SELECT * FROM books
                                WHERE Title LIKE "%{title}%"''')
            books = self.cursor.fetchall()
            return books
        except Exception as e:
            raise e
        

    def search_by_author(self, author):
        """Search the Author field in books for a specific word"""
        try:
            # Executes query
            self.cursor.execute(f'''SELECT * FROM books
                                WHERE Author LIKE "%{author}%"''')
            books = self.cursor.fetchall()
            return books
        except Exception as e:
            raise e
        

    def search_by_id(self, id):
        """Search the Id field in books for a specific word"""
        try:
            # Executes query
            self.cursor.execute('''SELECT * FROM books
                                WHERE Id = ?''', (id,))
            books = self.cursor.fetchall()
            return books
        except Exception as e:
            raise e
        
    
    def delete_book(self, id):
        "Delete a book record from the books table"
        try:
            # Create delete querry
            self.cursor.execute('''DELETE FROM books
                                WHERE Id = ?''', (id,))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        

    def update_book(self, id, title, author, quantity):
        """Updates book record"""

        try:
            # Executes query
            self.cursor.execute('''UPDATE books
                                SET Title = ?, Author = ?, QTY = ?
                                WHERE Id = ?''', (title, author, quantity, id))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e