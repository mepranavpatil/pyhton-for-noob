#remove the duplicates in the list

list = [1, 2, 3, 4, 2, 3, 5, 1]
list.sort()
print(list)
new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)