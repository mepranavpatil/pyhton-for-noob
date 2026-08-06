#find the largest no.

# num=[10,56,78,45,23,45,887,96,35,23,56,788]
# for i in range(len(num)):
#         for j in range(i+1, len(num)):
#             if num[i] < num[j]:
#                 num[i], num[j] = num[j], num[i]
# print("The largest number is:", num[0])

num = [10, 56, 78, 45, 23, 45, 887, 96, 35, 23, 56, 788]
max = num[0]
for i in num:
    if i > max:
        max = i
print("The largest number is:", max)
