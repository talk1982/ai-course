print("Hello, engineers!")

#%%
print("Welcome to the world of coding.  Let's build something amazing together.")
# %%
# list all prime numbers from 1 to 100
for num in range(1, 101):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime and num > 1:
        print(num)

#%%
print ("one", "two", "three")
print("four")
print("five")
# %%
name = "Osnat"
age = 32
height = 1.61
is_student = True

print(f"{name} is {age} years old and {height}m tall.")
print("Hello".lower())

type(name)
# %%
x = 3
y = x * str(x)
print(y)
print(type(y))

# %%
print("Phyton", "\n", "data", "\n", "science")

# %%
print("C\:Python\number")
print("C:\\Python\\number")
print(r"C:\Python\number")
# %%
name = "Tal"
age = 42.2
height = 1.80
is_student = True

str1 = "Hey %s!" % (name)
print(str1)
str2 = "Hey %s, you are %d years old and %.2f m tall." % (name, age, height)
print(str2)

# %%
string = "We study Python for AI"
print("Given String:", string)
print('\nString Method index()')
print("Index of 'e' in:'", string, "':", string.index('e'))
print('\nString Method count()')
print("Count of 'o' in'", string, "':", string.count('o'))
print('\nString Method replace()')
print("Replacing 'e' with '3':", string.replace('e', '3'))
# %%
str ="foobar"
print(str[2:0]) #nothing printend
print(str[0:8])
print(str[7])
# %%
help(str.count)
dir(str) # constructors + methods 
# %%
import keyword
print(keyword.kwlist)
# %%
str1 = "We study Python for AI"
lst1 = str1.split()
print(lst1)
print(type(lst1))

lst2 = str1.split("o")
print(lst2)
lst3 = str1.split(" ")
print(lst3)
lst4 = str1.split(" ", 2)
print(lst4)
# %%
#Class exercise – Lecture 1
nameList = ["Amit", "Sharon", "Dana", "Sarah", "Tal"]
slicedNameList = nameList[:3]
print(slicedNameList)

#slicedNameList.pop(1) 
del slicedNameList[1]
print(slicedNameList)

slicedNameList.append("Osnat")
print(slicedNameList)

# %%
