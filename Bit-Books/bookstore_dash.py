'''This file contains all the code for the bookstore dashboard'''

# = = = = Imports = = = = #
import shared_functions

# = = = = Classes = = = = #
'''This section contain the classes'''

class Bookstore_Dash():
    """Class for the bookstore dashboard and sub menus"""

    


    def __init__(self, username, user_role):
        """Constructor"""
        self.username = username
        self.user_role = user_role

        # Activates main menu
        self.main_menu()


    def main_menu(self):
        """Displays two different menus. one for "Admin", and one for "Employee"."""
        # Clears console
        shared_functions.clear_console()
        # Displays header
        self.print_dashboard_header()
        self.main_menu_print(self.user_role)
        self.main_menu_option_select()
        
        
    def print_dashboard_header(self):
        """Prints the header of the dashboard"""
        # Prints business logo
        shared_functions.print_store_logo()
        # Prints user details that is logged in
        print(f'''| {self.username}, you are logged in as an "{self.user_role}"
===============================================================\n''')
        

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
                    break
                elif option == 2:
                    break
                elif option == 3:
                    break
                elif option == 4:
                    break
                elif option == 5 and self.user_role == "Admin":
                    break
                elif option == 6 and self.user_role == "Admin":
                    break
                elif option == 10:
                    break
                else:
                    # Clears console
                    shared_functions.clear_console()
                    # Displays header
                    self.print_dashboard_header()
                    print("*****(You did not insert a given option!)*****\n")
                    self.main_menu_print(self.user_role)

            # Loops and prints out menu again
            except Exception:
                # Clears console
                shared_functions.clear_console()
                # Displays header
                self.print_dashboard_header()
                print("*****(You did not insert a given option!)*****\n")
                self.main_menu_print(self.user_role)
                