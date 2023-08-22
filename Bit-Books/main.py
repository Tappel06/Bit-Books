'''This is the main file which runs the entire ebookstore program'''
# = = = = Imports = = = = #

# imports the login class
from login import Login
from bookstore_dash import Bookstore_Dash


# = = = = Run Program = = = = #

# Keeps program in the loop, for if users logout, but keep application running
while True:
    # Creates a new login object
    login = Login()
    # Creates dashboard object
    dashboard = Bookstore_Dash(login.username, login.role)
