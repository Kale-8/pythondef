# Utils
import re

from cloudinit.templater import JUndefined


def validation(value:any, condition,custom_alert:str='')->any:
    alert = lambda: print(f'\nThe number or character entered is incorrect, please enter it again.{custom_alert}')
    while True:
        try:
            if type(value) is str: value = value.lower().strip()
            if condition(value): return value
            alert()
        except ValueError: alert()

# 1. Library Book Tracker
library:dict = {}
def add_book(title:str,author:str,pages:int)->None:
    if title in library:
        print("Book already exists.")
        return
    library[validation(title, lambda x: re.search(r'^[a-z\d\s]+$', x, re.IGNORECASE),' Only letters, numbers and spaces between words are allowed')] = \
        {
        "author":validation(author, lambda x: re.search(r'^[a-z\d\s]+$', x, re.IGNORECASE),' Only letters, numbers and spaces between words are allowed'),
        "pages":validation(pages, lambda x: x >= 1,' The number of pages must be greater than 0')
        }
def find_book(title:str)->str:
    if title in library:
        return f"{title.title()} by {library[title]['author'].title()} has {library[title]['pages']} pages."
    else:
        return 'Book not found.'
def show_books()->None:
    if library:
        print(f"{'Title':<20}{'Author':^20}{'Pages':>10}")
        for title,book in library.items():
            print(f"{title.title():<20}{book['author'].title():^20}{book['pages']:>10}")
    else: print("No books found.")

#  2. Student Grade Manager
grades:dict = {}
def add_student(name:str)->None:
    if name in grades:
        print("Student already exists.")
        return
    grades[validation(name, lambda x: re.search(r'^[a-z\s]+$', x, re.IGNORECASE), ' Only letters and spaces between words are allowed')] = []
def add_grade(name:str, grade)->None:
    name = name.lower().strip()
    if name in grades:
        grade = validation(grade, lambda x: 0 <= x <= 100, ' The grade must be between 0 and 100')
        grades[name].append(grade)
    else: print("Student not found.")
def get_average(name:str)->any:
    name = name.lower().strip()
    if name in grades:
        if grades[name]: return sum(grades[name])/len(grades[name])
        else: return f'The student has no grades.'
    else:
        return"Student not found."

# # 3. Restaurant Menu Editor
# def change_availability(): pass
# def total_available_price(): pass
dish_list:dict = {}
def add_dish(dish:str,price:float,availability:bool)->None:
    if dish in dish_list:
        print("The dish already exists.")
        return
    dish_list[dish] = {"price":price,"availability":availability}
def change_availability(dish:str)->None:
    if dish in dish_list:
        dish_list[dish]["availability"] = not dish_list[dish]["availability"]
    else: print("Dish not found.")
def show_books()->None:
    if library:
        print(f"{'Title':<20}{'Author':^20}{'Pages':>10}")
        for title,book in library.items():
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
                              validation('\nEnter the number of pages the book has: ', lambda x: x >= 1,int, ' The number of pages must be greater than 0'))
                case 2:
                    find_book(str(input('\nEnter the name of the book you want to search for: ')))
                case 3: show_books()
                case 4: flag = False
                case _: print('\nInvalid option.')
        except ValueError: print('\nInvalid option.')
#book_menu()

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
