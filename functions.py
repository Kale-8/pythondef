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

# 2. Student Grade Manager
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

# 3. Restaurant Menu Editor
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

# 4. Warehouse Box Counter
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

# 5. Movie Rating System
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

# 6. Online Course Tracker
courses:dict = {}
def add_course(course:str,hours:int,enrolled:int)->None:
    if course in courses:
        print('The course already exists.')
        return
    courses[course] = {'hours':hours, 'enrolled':enrolled}
def update_enrollment(course:str,enrolled:int)->None:
    if course in courses:
        courses[course]['enrolled'] = enrolled
    else: print('The course doesnt exist.')
def filter_by_hours(hours:int):
    return {key: value for key, value in courses.items() if value['hours'] >= hours}

# 7. To-Do List Organizer
todos:dict = {}
def add_task(task:str,priority:str)->None:
    if task in todos:
        print('The task already exists.')
        return
    todos[task] = {'priority':priority, 'status':'uncompleted'}
def complete_task(task:str)->None:
    if task in todos:
        todos[task]['status'] = 'completed'
def filter_tasks(priority:str, status:str):
    return [key for key, value in todos.items() if value['priority'] == priority and value['status'] == status]

# 8. Digital Wallet
wallet:dict = {}
def add_expense(category:str,expense:float)->None:
    if category in wallet:
        wallet[category] += expense
    else: wallet[category] = expense
def total_spent()->float:
    return sum(wallet.values())
def expense_percentages()->dict:
    for category,expense in wallet.items():
        wallet[category] = expense/total_spent()*100
    return wallet

# 9. Pet Adoption Center
pets:list = []
def add_pet(name:str,species:str,age:int)->None:
    if name in pets:
        print('The pet already exists.')
        return
    pet = {'name':name, 'species':species, 'age':age}
    pets.append(pet)
def find_by_species(species:str)->list:
    return [i for i in pets if i['species'] == species]
def older_than(age:int)->list:
    return [i for i in pets if i['age'] > age]

# 10. Gym Membership System
members:dict = {}
def register_member(name:str,plan:str,payment:str)->None:
    if name in members:
        print('The member already exists.')
        return
    members[name] = {'plan':plan, 'payment':payment}
def change_plan(name:str,plan:str)->None:
    if name in members:
        members[name]['plan'] = plan
    else: print('The member doesnt exist.')
def unpaid_members()->dict:
    return {key: value for key, value in members.items() if value['payment'] == 'late'}