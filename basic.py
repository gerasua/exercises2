# Basicos de Python
print("For statement \n")
for i in range(1, 11):
    print(i)

print("\n While statement \n")
i = 1
while i <= 10:
    print(i)
    i += 1

print("\nComparative \n")
a = 10
b = 20

if a < b:
    print("{} is less than {}".format(a, b))
elif a == 20:
    print("{} is iqual to {}".format(a, b))
else:
    print("{} is greater than {}".format(a, b))