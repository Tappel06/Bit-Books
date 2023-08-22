'''This file contains all the code for the bookstore dashboard'''

# = = = = Imports = = = = #
import shared_functions
from bookstore_database import Bookstore_database


# = = = = Classes = = = = #
'''This section contain the classes'''

class Bookstore_Dash():
    """Class for the bookstore dashboard and sub menus"""

    def __init__(self, username, user_role):
        """Constructor"""
        # Creates username variable
        self.username = username
        # Creates user_Role Variable
        self.user_role = user_role

        # Creates bookstore object
        self.bookstore_db = Bookstore_database()

        # Activates main menu
        self.main_menu()

    
    #===Main Menu Section===#
    '''This section contains all the methods regarding the main menu and its options'''

    def main_menu(self):
        """Displays two different menus. one for "Admin", and one for "Employee"."""

        # Displays header
        self.print_dashboard_header()
        # Prints user and its role
        self.main_menu_print(self.user_role)
        # Opens the main Menu
        self.main_menu_option_select()
        

    def main_menu_print(self, user_role):
        """Prints two different menus. one for admin, and one for clerk/employee"""

        # Checks if Admin or Employee
        if user_role == "Admin":
            print('''Choose an option:
                  
1. Enter book
2. Update book
3. Delete book
4. Search books
5. Add a user
6. Remove a user
10. Logout
0. Exit''')
        elif user_role == "Employee":
            print('''Choose an option:
                  
1. Enter book
2. Update book
3. Delete book
4. Search books
10. Logout
0. Exit''')
        
        else: 
            # Automatically exits program if security layer has been bypassed
            exit()


    def main_menu_option_select(self):
        
        """Redirects user to correct menus, determined by role"""

        # Loops til right condition is found
        while True:
            # Checks wether option is an integer
            try:
                # Takes int value
                option = int(input("\nOption: "))

                # Assign options to specific users
                if option == 0:
                    exit()

                elif option == 1:
                    self.enter_book_options()
                    # Displays header
                    self.print_dashboard_header()
                    # Prints user and its role
                    self.main_menu_print(self.user_role)

                elif option == 2:
                    # Displays header
                    self.print_dashboard_header()
                    # Prints user and its role
                    self.main_menu_print(self.user_role)

                elif option == 3:
                    # Displays header
                    self.print_dashboard_header()
                    # Prints user and its role
                    self.main_menu_print(self.user_role)

                elif option == 4:
                    self.find_books_options()
                    # Displays header
                    self.print_dashboard_header()
                    # Prints user and its role
                    self.main_menu_print(self.user_role)

                elif option == 5 and self.user_role == "Admin":
                    # Displays header
                    self.print_dashboard_header()
                    # Prints user and its role
                    self.main_menu_print(self.user_role)

                elif option == 6 and self.user_role == "Admin":
                    # Displays header
                    self.print_dashboard_header()
                    # Prints user and its role
                    self.main_menu_print(self.user_role)

                elif option == 10:
                    # Do not remove "break". It helps with logout
                    break

                else:
                    # Clears console
                    shared_functions.clear_console()
                    # Displays header
                    self.print_dashboard_header()
                    print("\x1b[31m*****(You did not insert a given option!)*****\x1b[0m\n")
                    self.main_menu_print(self.user_role)

            # Loops and prints out menu again
            except Exception:
                # Clears console
                shared_functions.clear_console()
                # Displays header
                self.print_dashboard_header()
                print("\x1b[31m*****(You did not insert a given option!)*****\x1b[0m\n")
                self.main_menu_print(self.user_role)


    #===Enter book Section===#
    '''This section contains all the methods for inserting a new book'''

    def enter_book_options(self):
        """Displays  the options for a new book being entered"""
        
        # Variable for book id
        id = self.bookstore_db.get_unassigned_id()
        # Variable for title
        global title
        title = ""
        # Variable for author
        global author
        author = ""
        # Variable number of copies
        global copies
        copies = 0

        # Prints dashboard header
        self.new_book_options_reprint(id, title, author, copies)

        # Loops the options
        while True:
            try:
                # Prints Options
                option = int(input("Option: "))

                # Options
                if option == 0:
                    # Exits back to main menu
                    break

                elif option == 1:
                    # Gets input of title
                    title = input("Please insert the title: ")
                    # rerun loop
                    self.new_book_options_reprint(id, title, author, copies)

                elif option == 2:
                    # Gets input of author
                    author = input("Please insert the Author: ")
                    # rerun loop
                    self.new_book_options_reprint(id, title, author, copies)

                elif option == 3:
                    try:
                        copies = int(input("Please insert amount of copies: "))
                        # rerun loop
                        self.new_book_options_reprint(id, title, author, copies)

                    except Exception:
                        # Prints Dashboard
                        self.print_dashboard_header()
                        # Prints book details
                        self.print_new_book_details(id, title, author, copies)
                        print("\x1b[31m*****(You did not insert a number!)*****\x1b[0m\n")
                        self.print_new_book_options()

                elif option == 4:
                    # Checks for incomplete data
                    if title == "" or author == "":
                        self.print_new_book_details(id, title, author, copies)
                        print("\x1b[31m*****(Cannot Save, some details are empty!)*****\x1b[0m\n")
                        self.print_new_book_options()

                    else:

                        # Adds new book to the books table in the database
                        self.bookstore_db.insert_new_book_record(id, title, author, copies)
                        # Reassign a new ID
                        id = self.bookstore_db.get_unassigned_id()
                        # Resets title
                        title =""
                        # Resets Author
                        author = ""
                        # Resets copies
                        copies = 0

                        #Print the book details again, and also acknowledges record added
                        self.print_new_book_details(id, title, author, copies)
                        print(f"\x1b[34m*****(New Book stored into system!)*****\x1b[0m\n")
                        self.print_new_book_options()

                    pass
                else:
                    # Prints Dashboard
                    self.print_dashboard_header()
                    # Prints book details
                    self.print_new_book_details(id, title, author, copies)
                    print("\x1b[31m*****(You did not insert a given option!)*****\x1b[0m\n")
                    self.print_new_book_options()

            except Exception:
                # Prints Dashboard
                self.print_dashboard_header()
                # Prints book details
                self.print_new_book_details(id, title, author, copies)
                print("\x1b[31m*****(You did not insert a given option!)*****\x1b[0m\n")
                self.print_new_book_options()


    def new_book_options_reprint(self, assigned_id, book_title, book_author, book_copies):
        """reprint the details for new_book menu"""
        self.print_dashboard_header()
        self.print_new_book_details(assigned_id, book_title, book_author, book_copies)
        self.print_new_book_options()


    def print_new_book_details(self, id = 0, title = "", author = "", copies = 0):
        """Displays the details of the new book so far"""

        # Prints dashboard header
        self.print_dashboard_header()
        # Prints the details of the new book being entered
        print(f'''New book details:
              
Auto-assigned ID: {id}
Title: {title} 
Author: {author}
Copies: {copies}
===============================================================''')


    def print_new_book_options(self):
        """Prints the options available for new book"""

        # Prints options
        print('''Choose an Option:
              
1. Add title
2. Add author
3. Add total number of copies
4. Save
0. Main menu\n''')


    #===Find books section===#
    '''Contains all the methods regarding finding books'''

    def find_books_options(self):
        """Display all the options for finding books"""

        # Display dashboard header
        self.print_dashboard_header()
        # Display Options
        self.find_Books_options_display()

        # Loops inputs
        while True:
            try:
                # Gets option input
                option = int(input("Option: "))

                # Executes the functions according to option's input
                if option == 0:
                    # Do not remove break, It helps with returning to main Menu
                    break

                elif option == 1:
                    # Displays all records of books
                    break

                elif option == 2:
                    # Allows to search by title
                    break

                elif option == 3:
                    # Allows to search by author
                     break
                
                elif option == 4:
                    # Retrieves a book according to ID
                    break

                else:
                    # Clears console
                    shared_functions.clear_console()
                    # Displays header
                    self.print_dashboard_header()
                    print("\x1b[31m*****(You did not insert a given option!)*****\x1b[0m\n")
                    self.find_Books_options_display()

            except Exception:
                # Clears console
                shared_functions.clear_console()
                # Displays header
                self.print_dashboard_header()
                print("\x1b[31m*****(You did not insert a given option!)*****\x1b[0m\n")
                self.find_Books_options_display()


    def find_Books_options_display(self):
        """Prints Out the options for Finding books options"""
        # Prints dashboard header
        print('''Choose a search option:
              
1. View all Books
2. Search by title
3. Search by author
4. Search by ID
0. Main menu\n''')


    #===Shared Methods===#
    '''This section contains methods shared with the rest of the methods'''

    def print_dashboard_header(self):
        """Prints the header of the dashboard"""
        # Clears console
        shared_functions.clear_console()
        # Prints business logo
        shared_functions.print_store_logo()
        # Prints user details that is logged in
        print(f'''{self.username}, you are logged in as an "{self.user_role}"
===============================================================''')
