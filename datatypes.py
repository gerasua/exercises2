# Datatypes

# Lists
my_list = [10, 20, 30, 40, 50]
print("Lists")
print("my_list = [10, 20, 30, 40, 50]")
for i in my_list:
    print(i)
print("\n")

# Tuples
my_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Tuplas")
print("my_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)")
for i in my_tup:
    print(i)
print("\n")

# Dict
my_dict = {'name': 'Bronx', 'Age': '2', 'ocupation': "Corey's Dog"}
print("Dict")
print("my_dict = {'name': 'Bronx', 'Age': '2', 'ocupation': \"Corey's Dog\"}")
for key, val in my_dict.items():
    print("My {} is {}".format(key, val))
print("\n")

# Set
my_set = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}
print("Set")
print("my_set = {10, 20, 30, 40, 50, 10, 20, 30, 40, 50}")
for i in my_set:
    print(i)