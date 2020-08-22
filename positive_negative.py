# Program to seperate the positive and negative numbers of an array.

inp_str = input("Enter the elements of the array (seperated by spaces) :")

array_list = inp_str.split()
array_list = [int(x) for x in array_list]
neg_array_list = []
pos_array_list = []

for i in array_list:
    if i < 0:
        neg_array_list.append(i)
    else:
        pos_array_list.append(i)

pos_array_list.sort()
neg_array_list.sort()
print("\nThe Positive numbers in the entered array are: ")
print(pos_array_list)
print("\nThe Negative numbers in the entered array are: ")
print(neg_array_list)
