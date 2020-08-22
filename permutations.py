# Write a program to show all the permutations of given 4 numbers

count = 0

inp = input("Enter 4 numbers:(with spaces in between each number):")
num = inp.split()

# check input size for exactly 4 numbers?
print("Permutations :\n")
i = 0
while (i <= 3):
    j = 0
    while(j <= 3):
        if (i == j):
            j = (j + 1) % 4
        for a in [0, 1, 2, 3]:
            if a != i and a != j:
                k = a
                break
        for b in [0, 1, 2, 3]:
            if b != i and b != j and b != k:
                x = b
                break
        print(num[i], num[j], num[k], num[x])
        print(num[i], num[j], num[x], num[k])
        count = count+2
        if count == 24:
            break
        j = j+1
    i = i+1

print('done')
