# Utils
import re

def validation(text:str, condition, data_type,custom_alert:str='')->str or float or int:
    alert = lambda: print(f'\nThe number or character entered is incorrect, please enter it again.{custom_alert}')
    while True:
        try:
            value:data_type = data_type(input(f'\n{text}'))
            if data_type == str: value = value.lower().strip()
            if condition(value): return value
            alert()
        except ValueError: alert()

# 1. Library Book Tracker
book_list:dict = {}
def add_book(title:str,author:str,pages:int)->None:
    if title.lower().strip() in book_list:
        print("Book already exists.")
        return
    book_list[title] = {"author":author,"pages":pages}
def find_book(title:str)->None:
    if title in book_list:
        print(f"{title.title()} by {book_list[title]['author'].title()} has {book_list[title]['pages']} pages.")
    else: print("Book not found.")
def show_books()->None:
    if book_list:
        print(f"{'Title':<20}{'Author':^20}{'Pages':>10}")
        for title,book in book_list.items():
            print(f"{title.title():<20}{book['author'].title():^20}{book['pages']:>10}")
    else: print("No books found.")
def book_menu()->None:
    flag:bool = True
    while flag:
        try:
            option:int = int(input(f'\n1. Add book\n2. Find book\n3. Show books\n4. Exit\nEnter an option: '))
            match option:
                case 1:
                    add_book(validation('\nEnter the name of the book: ', lambda x: re.search(r'^[a-z\d\s]+$', x, re.IGNORECASE) ,str, ' Only letters, numbers and spaces between words are allowed'),
                              validation('\nEnter the author of the book: ', lambda x: re.search(r'^[a-z\d\s]+$', x, re.IGNORECASE) ,str, ' Only letters, numbers and spaces between words are allowed'),
                              validation('\nEnter the number of pages the book has: ', lambda x: x >= 1,float, ' The number of pages must be greater than 0'))
                case 2:
                    find_book(str(input('\nEnter the name of the book you want to search for: ')))
                case 3: show_books()
                case 4: flag = False
                case _: print('\nInvalid option.')
        except ValueError: print('\nInvalid option.')
#book_menu()

#  2. Student Grade Manager
# def add_student(): pass
# def add_grade(): pass
# def get_average(): pass
#
# # 3. Restaurant Menu Editor
# def add_dish(): pass
# def change_availability(): pass
# def total_available_price(): pass
#
# # 4. Warehouse Box Counter
# def add_box(): pass
# def update_quantity(): pass
# def has_enough(): pass
#
# # 5. Movie Rating System
# def add_movie(): pass
# def rate_movie(): pass
# def average_rating(): pass
#
# # 6. Online Course Tracker
# def add_course(): pass
# def update_enrollment(): pass
# def filter_by_hours(): pass
#
# # 7. To-Do List Organizer
# def add_task(): pass
# def complete_task(): pass
# def filter_tasks(): pass
#
# # 8. Digital Wallet
# def add_expense(): pass
# def total_spent(): pass
# def expense_percentages(): pass
#
# # 9. Pet Adoption Center
# def add_pet(): pass
# def find_by_species(): pass
# def older_than(): pass
#
# # 10. Gym Membership System
# def register_member(): pass
# def change_plan(): pass
# def unpaid_members(): pass
