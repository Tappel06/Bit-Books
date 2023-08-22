'''This file handles the user database'''

# = = = = Imports = = = = #
import sqlite3
import os


# = = = = Class = = = = #

class User_database():
    '''This Class handles the connection to the user database'''

    def __init__(self):
        """Constructor"""

        # Checks wether "user_db" exists, then create a default DB if not
        if self.user_db_exists() == False:
            # Creates directory if it does not exist
            if os.path.exists("Users") != True:
                os.mkdir("Users")
                
            # Creates user_db
            self.db = sqlite3.connect('Users/users_db')
            self.cursor = self.db.cursor()

            # Creates users table
            self.create_Table()
            # Creates users, one admin and two employees
            self.insert_new_user_record(1, "Admin", "Adm1n@1234", "Admin")
            self.insert_new_user_record(2, "John", "Cena", "Employee")
            self.insert_new_user_record(3, "Elon", "Musk", "Employee")

        # Connects or create the user db
        self.db = sqlite3.connect('Users/users_db')
        self.cursor = self.db.cursor()

    
    def create_Table(self):
        """Creates the default Users table"""
        try:
            self.cursor.execute('''
                                CREATE TABLE users(
                                Id INT(3),
                                Username VARCHAR(15),
                                Password VARCHAR(15),
                                Role VARCHAR(15),
                                PRIMARY KEY (Id)
                                );''')
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        

    def insert_new_user_record(self, id, username, password, role):
        """Inserts new user details into user_database"""
        try:
            self.cursor.execute('''INSERT INTO users
                                VALUES (?, ?, ?, ?)''', 
                                (id, username, password, role))
            self.db.commit()
            print(f"The folowing record has been inserted: {id}, {username}, {password}, {role}")
        except Exception as e:
            self.db.rollback()
            raise e
        

    def get_user_login(self, username, password):
        """Get user record where username and paswords match"""
        try:
            # Query
            self.cursor.execute('''SELECT * FROM users
                            WHERE Username = ? AND Password = ?''',
                            (username, password))
            user_record = self.cursor.fetchall()
        except Exception as e:
            return e
        
        return user_record


    def user_db_exists(self):
        """returns a True value if 'users_db' file exists"""
        exists = False

        try:
            with open("Users/users_db", "r") as file:
                exists = True
        except Exception:
            exists = False

        return exists





