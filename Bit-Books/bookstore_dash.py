'''This file contains all the code for the bookstore dashboard'''

# = = = = Imports = = = = #
import shared_functions
from bookstore_database import Bookstore_database
from user_database import User_database


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
        # Creates user object
        self.user_db = User_database()

        # Activates main menu
        self.main_menu()

    
# = = = = Main Menu Section = = = = #
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
                # Exit
                if option == 0:
                    exit()

                # Enter book
                elif option == 1:
                    self.enter_book_options()
                    # Displays header
                    self.print_dashboard_header()
                    # Prints user and its role
                    self.main_menu_print(self.user_role)

                # Update Book
                elif option == 2:
                    self.update_book_options()
                    # Displays header
                    self.print_dashboard_header()
                    # Prints user and its role
                    self.main_menu_print(self.user_role)

                # Delete book
                elif option == 3:
                    self.delete_book_options()
                    # Displays header
                    self.print_dashboard_header()
                    # Prints user and its role
                    self.main_menu_print(self.user_role)

                # Search books
                elif option == 4:
                    self.find_books_options()
                    # Displays header
                    self.print_dashboard_header()
                    # Prints user and its role
                    self.main_menu_print(self.user_role)

                # Add a new user
                elif option == 5 and self.user_role == "Admin":
                    self.add_new_user_options()
                    # Displays header
                    self.print_dashboard_header()
                    # Prints user and its role
                    self.main_menu_print(self.user_role)

                # Delete a user
                elif option == 6 and self.user_role == "Admin":
                    self.delete_user_options()
                    # Displays header
                    self.print_dashboard_header()
                    # Prints user and its role
                    self.main_menu_print(self.user_role)

                # Logout
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


# = = = = Enter book Section = = = = #
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


# = = = = Update book section = = = = #
    '''Contains all the methods regarding updating the books'''

    def update_book_options(self):
        """Displays the options for updating a book"""
        # Displays dashboard header
        self.print_dashboard_header()

        # asks for id input
        id = input("Please insert the id of the book you want to update: ")
        # Stores book record if it exists
        book = self.bookstore_db.search_by_id(id)
        
        # If book record exist
        if len(book) == 1:
            # Stores info into variable to alter it
            title = book[0][1]
            author = book[0][2]
            quantity = int(book[0][3])

            # Displays dashboard header
            self.print_dashboard_header()
            # Display current book record
            self.book_record_display(id, title, author, quantity)
            # Display update option
            self.print_update_options()

            # Loops options
            while True:
                # Option input
                option = input("Option: ")
                
                
                # Change title
                if option == "1":
                    title = input("New title: ")
                    # Displays dashboard header
                    self.print_dashboard_header()
                    # Display current book record
                    self.book_record_display(id, title, author, quantity)
                    # Prints change message
                    print("\x1b[36m*****(title changed!)*****\x1b[0m\n")
                    # Display update option
                    self.print_update_options()

                # Change author
                elif option == "2":
                    author = input("New Author: ")
                    # Displays dashboard header
                    self.print_dashboard_header()
                    # Display current book record
                    self.book_record_display(id, title, author, quantity)
                    print("\x1b[36m*****(Author changed!)*****\x1b[0m\n")
                    # Display update option
                    self.print_update_options()
                    
                # Change quantity
                elif option == "3":
                    try: 
                        quantity = int(input("New quantity: "))
                        # Displays dashboard header
                        self.print_dashboard_header()
                        # Display current book record
                        self.book_record_display(id, title, author, quantity)
                        print("\x1b[36m*****(Quantity changed!)*****\x1b[0m\n")
                        # Display update option
                        self.print_update_options()
                    except Exception:
                        # Displays dashboard header
                        self.print_dashboard_header()
                        # Display current book record
                        self.book_record_display(id, title, author, quantity)
                        print("\x1b[32m*****(You must insert a number!)*****\x1b[0m\n")
                        # Display update option
                        self.print_update_options()

                # Update changes
                elif option == "4":
                    self.bookstore_db.update_book(id, title, author, quantity)
                    # Displays dashboard header
                    self.print_dashboard_header()
                    print("\x1b[36m*****(Book updated!)*****\x1b[0m\n")
                    break

                # Return to previous menu
                elif option == "0":
                    break
                # error message
                else:
                    # Displays dashboard header
                    self.print_dashboard_header()
                    # Display current book record
                    self.book_record_display(id, title, author, quantity)
                    print("\x1b[32m*****(You must insert a given option!)*****\x1b[0m\n")
                    # Display update option
                    self.print_update_options()

        # If book record does not exist
        else:
            # Return to previous option
            print("\x1b[32m*****(This ID does not exist!)*****\x1b[0m\n")
            self.return_to_previous_menu()


    def print_update_options(self):
        """Prints the update options"""
        print('''Please select an update option:
              
1. Change title
2. Change author
3. Change quantity
4. Update changes
0. Cancel update''')

# = = = = Delete book section = = = = #
    '''Contains all the methods regarding deleting books'''

    def delete_book_options(self):
        """Deletes a specific book by id"""
        
        # Display dashboard header
        self.print_dashboard_header()

        while True:
            # Insert the id of the book
            id = input("Insert the ID of the book you want to delete: ")
            book = self.bookstore_db.search_by_id(id)

            # Checks if book exists
            if len(book) == 1:
                self.book_record_display(book[0][0], book[0][1], book[0][2], book[0][3])
                print(f"You are about to delete {book[0][1]} by {book[0][2]}")
                # input choise yes or no
                choice = input("Are you sure? (Y/N): ")
                # Delete if "Y"
                if choice.upper() == "Y":
                    self.bookstore_db.delete_book(id)
                    print("\x1b[34m*****(Book Deleted!)*****\x1b[0m\n")
                    break
                elif choice.upper() == "N":
                    print("\x1b[31m*****(Book not deleted!)*****\x1b[0m\n")
                    break
                else:
                    self.print_dashboard_header()
                    print("\x1b[31m*****(You did not insert a given option!)*****\x1b[0m\n")
            else:
                print("\x1b[31m*****(No such ID exists!)*****\x1b[0m\n")
                break

        # Return to previous menu
        self.return_to_previous_menu()


# = = = = Find books section = = = = #
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
                    # display all books
                    self.display_all_books()
                    # Display dashboard header
                    self.print_dashboard_header()
                    # Display Options
                    self.find_Books_options_display()

                elif option == 2:
                    # Allows to search by title
                    self.display_specific_books(2)
                    # Display dashboard header
                    self.print_dashboard_header()
                    # Display Options
                    self.find_Books_options_display()

                elif option == 3:
                    # Allows to search by author
                    self.display_specific_books(3)
                    # Display dashboard header
                    self.print_dashboard_header()
                    # Display Options
                    self.find_Books_options_display()
                
                elif option == 4:
                    # Retrieves a book according to ID
                    self.display_specific_books(4)
                    # Display dashboard header
                    self.print_dashboard_header()
                    # Display Options
                    self.find_Books_options_display()

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


    def display_all_books(self):
        """Displays all the books in the database"""

        # Display dashboard header
        self.print_dashboard_header()
        print("\n*****This is all the books in the database*****\n")
        print("\nPress 'b' to go back\n")

        # Stores a list of all the books
        books = self.bookstore_db.get_all_book_records()
        # Prints each book into its own printed diplay record
        for i in range(len(books)):
            self.book_record_display(books[i][0], books[i][1], books[i][2], books[i][3])

        # input to return to previous menu
        self.return_to_previous_menu()


    def display_specific_books(self, title_or_autor):
        """Displays books being searched either by title or author"""
        # Checks for option 2, 3, or 4
        # If option 2, search by title
        if title_or_autor == 2:
            # Print dashboard header
            self.print_dashboard_header()
            search_title = input("Enter the title you are searching for: ")
            # Gets a list of books with simular title
            books = self.bookstore_db.search_by_title(search_title)
            # Prints a list of books simular to the search results
            for i in books:
                self.book_record_display(i[0],i[1],i[2],i[3],)
            # Input to return to previous menu
            self.return_to_previous_menu()

        # if option 3, search by author
        elif title_or_autor == 3:
            # Print dashboard header
            self.print_dashboard_header()
            search_author = input("Enter the author you are searching for: ")
            # Gets a list of books with simular title
            books = self.bookstore_db.search_by_author(search_author)
            # Prints a list of books simular to the search results
            for i in books:
                self.book_record_display(i[0],i[1],i[2],i[3],)
            # Input to return to previous menu
            self.return_to_previous_menu()

        # if option 4, search by id
        elif title_or_autor == 4:
            # Print dashboard header
            self.print_dashboard_header()
            search_id = input("Enter the id you are searching for: ")
            # Gets a list of books with simular title
            books = self.bookstore_db.search_by_id(search_id)
            # Prints a list of books simular to the search results
            for i in books:
                self.book_record_display(i[0],i[1],i[2],i[3],)
            # Input to return to previous menu
            self.return_to_previous_menu()


# = = = = Add new user Methods = = = = #
    '''Contains all methods regarding adding a new user'''

    def add_new_user_options(self):
        """adds a new user"""
        # Clears console
        self.print_dashboard_header()
        print("New user names cannot be \x1b[31m\"Admin\"\x1b[0m or \x1b[31m\"cancel\"\x1b[0m\n")

        # Assign an automated ID
        new_id = self.user_db.get_unassigned_id()
        
        # Loops input
        while True:
            # Inputs new username
            new_username = input("Insert new username: ")
            # Checks that username does not equal to Admin or cancel
            if new_username == "Admin" or new_username == "cancel":
                print("\x1b[31mNew user names cannot be \"Admin\" or \"cancel\"\x1b[0m\n")
            else:
                break

        # Inputs new password
        new_password = input("\nInsert new password: ")

        # Loops input
        while True:
            # Assign role
            role = input("Choose a role:\n1. Admin\n2. Employee\nOption: ")
            
            # if 1 then Admin
            if role == "1":
                role = "Admin"
                break

            # if 2 then Employee
            elif role == "2":
                role = "Employee"
                break

            # Else print input error message
            else:
                print("\x1b[31mYou did not insert a given option\x1b[0m\n")

        # Adds new user
        self.user_db.insert_new_user_record(new_id, new_username, new_password, role)

        # Clears console
        self.print_dashboard_header()
        # Prints that new user has been added
        print(f"\x1b[36m*****New user {new_username} has been added to the system as an {role}\x1b[0m\n")
        # return option
        self.return_to_previous_menu()


# = = = = Delete a user = = = = #
    ''' Contains all methods regarding adding a new user'''

    def delete_user_options(self):
        """display options to delete a user"""

        # Clears console
        self.print_dashboard_header()
        # Displays all user
        self.display_all_users()

        # Loops input
        while True:
            # Takes ID input
            id_delete = input("""Enter the ID of the user you want to delete.
Or type \"cancel\" to go back to previous menu.
ID: """)
            # if "cancel" is typed, break
            if id_delete == "cancel":
                break

            # If Id is equal to 1, indicate that "Admin cannot be deleted
            elif id_delete == "1":
                print("\x1b[31m*****(This user is not allowed to be deleted!)*****\x1b[0m\n")
            
            # checks if int
            elif self.checks_if_int(id_delete) == True:
                # Checks if Id exist
                if self.user_db.id_exists(int(id_delete)) == True:
                    # Delete user
                    self.user_db.delete_user_by_id(int(id_delete))
                    # Clear console
                    self.print_dashboard_header()
                    print("\x1b[31m*****(User deleted!)*****\x1b[0m\n")
                    # Exits loop
                    break

                else:
                    print("\x1b[31m*****(ID does not exist!)*****\x1b[0m\n")
        
        # return to previous menu option
        self.return_to_previous_menu()
        

    def checks_if_int(self, input):
        """checks if and input is a int"""
        try:
            int(input)
            return True
        except Exception:
            return False


    def display_all_users(self):
        """Displays all the users"""

        print("All Users")
        # Gets the list of users
        list = self.user_db.get_all_users()
        # Prints all of the records
        for record in list:
            print(f'''---------------------------------------------------------------
ID: {record[0]}
Username: {record[1]}
Role: {record[3]}
---------------------------------------------------------------''')


# = = = = Shared Methods = = = = #
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
        

    def book_record_display(self, id, title, author, quantity):
        """This is the common display in which a book record will be displayed"""
        print(f'''---------------------------------------------------------------
ID: {id}
Title: {title} 
Author: {author}
Quantity: {quantity}
---------------------------------------------------------------''')


    def return_to_previous_menu(self):
        """This method give the return to previous menu option"""
        # input to return to previous menu
        while True:
            back = input("Press'b' to go back: ")
            if back == "b":
                break
            else: 
                print("You need to press 'b' to go back")
