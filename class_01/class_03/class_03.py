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
