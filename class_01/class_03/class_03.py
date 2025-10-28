# %%
#values = [10, 20, 30, 40, 50]
values = "abc"
#values = set(["a", "b", "c", "d"])
for count, value in enumerate(values):
    print(count, value)
# %%

patientId = ['001222', '001422', '001224', '001223']
illness = ['Diabetes', 'Hypertension', 'Asthma', 'Allergy']
for q, a in zip(patientId, illness):
    print('The patient id:', q, 'has illness:', a)
# %%

def hello():
    """This is a sample function that 
        returns a greeting message."""
    return "Hello, World!"

help(hello)
# %%
def add_numbers():
    x=2
    y=4
    print(x,y)
    return(x+y)

add_numbers()
# %%
def seven():
    "return the number 7"
    x= 7
    return x

seven()
# %%

def add_number(x, y):
    "sum 2 numbers"
    return x,y, x+y

print(add_number("3","5.0"))
type(add_number)
type(add_number(3,4.5))
# %%
def add_numbers(n1=100, n2=1000):
    sum = n1+n2
    return sum

result = add_numbers(5.4)
print(result)
# %%
def foo(*args):
    print(args)

foo(1,2,3,4,5)
# %%
def my_sum(*integers):
    result=0
    for x in integers:
        result += x
    return result
    
print(my_sum(1,2,3,4))
# %%

def my_functions(**Patient):
    print("Her last name is "+ Patient["lname"])
    print(type(Patient))

my_functions(fanme = "Maya", lname = "Malmud")
# %%
def decoratorTal(func):

    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper

@decoratorTal
def greet():
    print("Hello, World1")

greet()
# %%

data = [i**2 for i in range(10)]
print(data)

squards = [i**2 for i in range(10) if i%2 == 0]
print(squards)
# %%
f = lambda x: 2*x+1
f(5)
# %%
def cube(x):
    return x*x*x

list(map(cube, range(10)))
#like for 
# %%

def filter_vowels(variable):
    letters = ['a']
    if(variable in letters):
        return True
    else:
        return False

sequence = "encyclopedia"
list(filter(filter_vowels, sequence))
# %%

from functools import reduce
lst = [1,2,3,4]

product = reduce((lambda x, y: x*y),lst)

print(product)
# %%
books = [ 
    {"title": "Python 101", "price": 39.99, "rating": 4.5}, 
    {"title": "Deep Learning", "price": 59.99, "rating": 4.8}, 
    {"title": "AI for Beginners", "price": 29.99, "rating": 4.2}, 
    {"title": "Data Science Daily", "price": 49.99, "rating": 3.9}, 
    {"title": "The Bug Book", "price": 19.99, "rating": 3.2} ]

def is_highly_rated(rating):
    if(rating >= 4.5):
        return True
    return False

for book in books:
    print("Book:") 
    for key, value in book.items(): 
        print(f" {key}: {value}" )
        if(key == "rating"):
            print(f" Is highly rated? -> {is_highly_rated(book["rating"])}")



def get_top_books(book_list):
    "# Write a function get_top_books(book_list) that uses the first function to filter top-rated books."
    finalList = []
    for book in book_list:
        for bookKeys in book:
            if(bookKeys == "rating"):
                if(is_highly_rated(book[bookKeys])):
                    finalList.append(book)
    return finalList

print(get_top_books(books))

#Use the sorted() function to sort Books by rating (high to low) and print the top 3 results.
def get_key(book):
    for key, value in book.items():
        if key == "price":
            return value

 
print(f"{sorted(books, key = get_key, reverse=True)}")

#Magic functions: Use map() with a lambda to round all book prices to the nearest integer.
rounded_prices = list(map(lambda dic_book: round(dic_book["price"]), books))
print(f" --- {rounded_prices}")
#Use filter() to keep books under $40

adorable_book = list(filter(lambda x: x["price"]<40, books))
print(adorable_book)
print([book["title"] for book in adorable_book])
# %%
