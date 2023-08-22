'''This file cotains the codes that help with user authentication and login to the bookstore'''
'''Will contain two options:
1. Admin Login
2. Clerk Login'''

# = = = = Imports = = = = #
from user_database import User_database
import shared_functions


# = = = = Class = = = = #
class Login():
    '''handles the authentication of the users'''
    username = ""
    role = ""
    logged_in = False

    def __init__(self):
        "Constructor"

        # Creates User_databse object
        self.user_db = User_database()

        # login_menu
        self.login_menu()


    #===Methods===#
    def login_menu(self):
        "The login menu"

        # Clears console
        shared_functions.clear_console()
        # Prints store logo
        shared_functions.print_store_logo()
        print("\nLogin")

        # Takes and validates user input, then login user
        while True:
            # Asks username input
            user_name = input("\nUsername: ")
            # Asks password input
            pass_word = input("Password: ")

            # User record
            user_record = self.user_db.get_user_login(user_name, pass_word)
            
            # Validates user
            if len(user_record) == 1:
                print(user_record[0][0])
                self.username = user_record[0][1]
                self.role = user_record[0][3]
                self.logged_in = True
                print(f"Username = {self.username}\nRole = {self.role}\nLogged in = {self.logged_in}")
                break
            else:
                # Clears console
                shared_functions.clear_console()
                # Prints store logo
                shared_functions.print_store_logo()
                print("\nLogin (The username or password is incorrect.) ")
        


    


# = = = = Functions = = = = #




