
from datetime import datetime, timedelta

class Book:
    def __init__(self, id, title, author, genre, available=True, due_date=None, checkouts=0):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.available = available
        self.due_date = due_date
        self.checkouts = checkouts
    
    def display_info(self):
        print(f'ID: {self.id}')
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print('-' * 40)

    def checkout(self):
        if not self.available:
            print(f'{self.title} is already checked out.')
            return
        self.available = False
        self.due_date = (datetime.today() + timedelta(weeks=2)).strftime('%Y-%m-%d')
        self.checkouts += 1
        print(f'{self.title} has been checked out. Due back on {self.due_date}.')

    def is_overdue(self):
        if self.available or not self.due_date:
            return False
        due = datetime.strptime(self.due_date, '%Y-%m-%d').date()
        return due < datetime.today().date()
    
    def return_book(self): # makes book available again
        if self.available:
            print(f'{self.title} was not checked out')
            return
        self.available = True
        self.due_date = None
        print(f'{self.title} has been returned')
# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
from library_books import library_books

books = [Book(**b) for b in library_books]

def view_available_books():
    available = [b for b in books if b.available] # defines the books that are available
    if not available:    
        print('No books are currently available.')
        return
    print('Available Books:')
    print('-' * 40)
    for b in available:
        b.display_info()
# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books(search_term):
    # term and the results
    term = search_term.lower()
    results = [b for b in books if term in b.author.lower() or term in b.genre.lower()] # case-insensitive
    if not results:
        print('No matching books found.') # if there are no matching books
        return
    print('Search Results: ')
    print('-' * 40) # border
    for b in results:
        b.display_info()



# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def check_out(book_id):
    for b in books: # goes through all books
        if b.id.lower() == book_id.lower(): # if the book ids match
            b.checkout() # checkout if possible
            return
    print('Book ID not found')
                


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

def return_book(book_id):
    for b in books: # goes through all books
        if b.id.lower() == book_id.lower(): # if the book ids match
            b.return_book() # return book if possible
            return
    print('Book ID not found')
# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def list_overdue_books():
    overdue = [b for b in books if b.is_overdue()] # gets overdue books
    if not overdue:
        print('No overdue books.') # if user dont have overdue books
        return
    print('Overdue Books:') # if they do they can see them
    print('-' * 40)
    for b in overdue:
        print(f'{b.title} (was due {b.due_date})')

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.



# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

def top_checked_out_books():
    top_three = sorted(books, key=lambda x: x.checkouts, reverse=True)[:3] # algorithm
    print('Top 3 Most Checked-Out Books:') # display
    print('-' * 40)
    for b in top_three:
        print(f'{b.title} - {b.checkouts} checkouts') 

def menu():
    while True:
        print('\nMenu:') # options for user
        print('1. View Available Books')
        print('2. Search by Author or Genre')
        print('3. Checkout a Book')
        print('4. Return a Book')
        print('5. View Overdue Books')
        print('6. View Top 3 Most Checked-Out Books')
        print('7. Quit')

        choice = input('Choose an option (1-7): ')
# actions for options
        if choice == '1':
            view_available_books()
        elif choice == '2':
            term = input('Enter author or genre: ')
            search_books(term)
        elif choice == '3':
            book_id = input('Enter book ID: ')
            check_out(book_id)
        elif choice == '4':
            book_id = input('Enter book ID: ')
            return_book(book_id)
        elif choice == '5':
            list_overdue_books()
        elif choice == '6':
            top_checked_out_books()
        elif choice == '7':
            print('Goodbye!')
            break
        else:
            print('Invalid choice, try again')
if __name__ == "__main__":
    menu()
    # manual testing 
