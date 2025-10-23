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