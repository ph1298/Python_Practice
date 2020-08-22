# Program to display the repeated elements of an array.

inp_Str = input("Enter the array elements (seperated by spaces) :")
array_List = inp_Str.split()
repeated_List = []

print("\nRepeated elements: ")
for i in array_List:
    if array_List.count(i) > 1:
        if i not in repeated_List:
            repeated_List.append(i)

repeated_List = [int(x) for x in repeated_List]
repeated_List.sort()
print(repeated_List)
