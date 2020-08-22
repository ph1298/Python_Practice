# Program to implement intersection and union of sets.

inp_set1 = input("Enter the elements of the set1 ( seperated by space ) :")
inp_set2 = input("Enter the elements of the set2 ( seperated by space ) :")

set1_list = inp_set1.split()
set2_list = inp_set2.split()

print("\nIntersection of the two sets: \n")
inter = []
for i in range(len(set1_list)):
    for j in range(len(set2_list)):
        if (set1_list[i] == set2_list[j]):
            inter.append(set1_list[i])
inter = [int(x) for x in inter]
inter.sort()
print(inter)

print("\nUnion of the two sets: \n")
union_set = []
for i in range(len(set1_list)):
    if (set1_list[i] not in set2_list):
        union_set.append(set1_list[i])

for j in range(len(set2_list)):
    if (set2_list[j] not in set1_list):
        union_set.append(set2_list[j])

union_final = []
union_final = union_set + inter
union_final = [int(x) for x in union_final]

union_final.sort()
print(union_final)
