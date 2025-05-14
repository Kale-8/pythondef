# 1. Library Book Tracker
library:dict = {}
def add_book(title:str,author:str,pages:int)->None:
    if title in library:
        print('Book already exists.')
        return
    library[title] ={'author':author, 'pages':pages}
def find_book(title:str)->str:
    if title in library:
        return f'{title.title()} by {library[title]['author'].title()} has {library[title]['pages']} pages.'
    else:
        return 'Book not found.'
def show_books()->None:
    if library:
        print(f'{'Title':<20}{'Author':^20}{'Pages':>10}')
        for title,book in library.items():
            print(f'{title.title():<20}{book['author'].title():^20}{book['pages']:>10}')
    else: print('No books found.')

#  2. Student Grade Manager
grades:dict = {}
def add_student(name:str)->None:
    if name in grades:
        print('Student already exists.')
        return
    grades[name] = []
def add_grade(name:str, grade:float)->None:
    if name in grades:
        grades[name].append(grade)
    else: print('Student not found.')
def get_average(name:str)->any:
    if name in grades:
        if grades[name]: return sum(grades[name])/len(grades[name])
        else: return f'The student has no grades.'
    else:
        return'Student not found.'

# # 3. Restaurant Menu Editor
menu:dict = {}
def add_dish(dish:str,price:float,availability:int)->None:
    if dish in menu:
        print('The dish already exists.')
        return
    menu[dish] = {'price':price, 'availability':availability}
def change_availability(dish:str)->None:
    if dish in menu:
        menu[dish]['availability'] = not menu[dish]['availability']
    else: print('The dish doesnt exist.')
def total_available_price()->float:
    if menu:
        return sum(dish['price'] for dish in menu.values() if dish['availability'])
    return 0

# # 4. Warehouse Box Counter
warehouse:dict = {}
def add_box(box:str,quantity:int)->None:
    if box in warehouse:
        print('The box already exists.')
        return
    warehouse[box] = {'quantity':quantity}
def update_quantity(box:str,quantity:int)->None:
    if box in warehouse:
        warehouse[box]['quantity'] = warehouse[box]['quantity'] + quantity
    else: print('The box doesnt exist.')
def has_enough(box:str,quantity:int)->bool:
    if box in warehouse:
        return warehouse[box]['quantity'] >= quantity
    else: return False

# # 5. Movie Rating System
# def add_movie(): pass
# def rate_movie(): pass
# def average_rating(): pass
movies:dict = {}
def add_movie(movie:str)->None:
    if movie in movies:
        print('The movie already exists.')
        return
    movies[movie] = []
def rate_movie(movie:str,rate:float)->None:
    if movie in movies:
        movies[movie].append(rate)
    else: print('The movie doesnt exist.')
def average_rating(movie:str)->float or str:
    if movie in movies:
        if movies[movie]: return sum(movies[movie])/len(movies[movie])
        else: return f'The movie has no ratings.'
    else:
        return'Movie not found.'

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
