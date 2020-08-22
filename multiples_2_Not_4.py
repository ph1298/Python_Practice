# Program to print the multiples of 2 that are not multiples of 4.

print("MULTIPLES OF 2 THAT ARE NOT MULTIPLES OF 4 :\n")

for i in range(100):
    if (i % 2 == 0) and (i % 4 != 0):
        print(i)
