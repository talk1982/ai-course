x=10
y=10

if x is y:
    print("x and y reference the same object in memory")
else:
    print("x and y reference different objects in memory")

x = ["a", "b", "c", "d"]
y = ["a", "b", "c", "d"]

print(x == y)  # True, because the contents are the same
print(x is y)  # False, because they are different objects in memory

# %%
print(3+4 == 14//2 and not 7 < 4.5) # true
# %%

var = ("geeks", "for", "geeks")
myTuple = ("geeks", )
print(type(var))
print(type(myTuple))
print("value in last index:", var[-1])
var[1]= "hello"  # This will raise a TypeError since tuples are immutable
# %%

tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c', 'd', 'e')
tuple3 = (tuple1 ,tuple2)
print("Concatenated Tuple:", tuple3)

# %%

print(tuple('phyton'))
print(list('phyton'))
# %%
tuple_1 = (1, 2, 3)
tuple_2 = ("yes","sure")

tuple_11 = tuple_1 + tuple_2
tuple_22 = tuple_1, tuple_2

print(len(tuple_11))
print(len(tuple_22))
# %%
x=""
if x!=0:
    print("True")
if x != None:
    print("True")
# %%
patients = [("Amit", 35), ("Dana", 17), ("Lior", 45), ("Sara", 22), ("Tom", 16)]

slicePatient = patients[:3]
print(slicePatient)

names = [name[0] for name in patients]
ages = [age[1] for age in patients]

print(names)
print(ages)

adult = []
for patient in patients:
    if patient[1] >= 18:
        adult.append( patient + (True,))
    else:
        adult.append( patient + (False,))
print(adult)

del patients[1]
print(patients)

patients.append( ("Nir", 29) )
print(patients)

if(names == None):
    print("Empty")
else:
    print(names)

print("Is names are empty = ", bool(names))
# %%

patient_ids = ["P001", "P002", "P003", "P004", "P005"]
test_results = [("Glucose", 88), ("Glucose", 98), ("Glucose", 828), ("Glucose", 25), ("Glucose", 15)]

dictionaryPatients = dict(zip(patient_ids, test_results))
print(dictionaryPatients)

for patientId in dictionaryPatients:
    if dictionaryPatients[patientId][1] > 90:
        print(f"Patient Id: {patientId}, the Glucose value is {dictionaryPatients[patientId][1]}")
    
# %%
