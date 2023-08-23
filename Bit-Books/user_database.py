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


    def get_unassigned_id(self):
        """Finds an ID that has not yet been assigned"""
        # Starting point where to start searching for an available id
        id = 2
        while True:
            
            try:
                self.cursor.execute('''SELECT * FROM users
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


    def get_all_users(self):
        "Gets all the users from users table"
        
        try: 
            # Execute query
            self.cursor.execute('''SELECT * FROM users;''')
            # Stores all the record into a list
            list = self.cursor.fetchall()
            # Returns the list
            return list
        except Exception as e:
            raise e


    def delete_user_by_id(self, id):
        """Deletes user by ID"""
        try:
            # Executes query
            self.cursor.execute('''DELETE FROM users
                                WHERE Id = ?;''', (id,))
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise e
        

    def id_exists(self, id):
        """Returns true if ID exists"""

        # Boolean set as False
        value = False
        try:
            # Execute query
            self.cursor.execute('''SELECT * FROM users
                                WHERE Id = ?;''', (id,))
            # Gets list
            list = self.cursor.fetchall()

            # Checks if list is equal to on
            if len(list) == 1:
                # turns value to True
                value = True
                # Return Value
                return value
            else:
                return value
        except Exception as e:
            raise e
        
    def print_answer(self, id):
        try:
            # Execute query
            self.cursor.execute('''SELECT * FROM users
                                WHERE Id = ?;''', (id,))
            # Gets list
            list = self.cursor.fetchall()
            if len(list) == 1:
                return True
            else:
                return False
            
        except Exception as e:
            raise e