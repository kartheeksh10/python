my_list = [1, 2, 3, 4, 5]

# Identity operators
a = my_list
b = [1, 2, 3, 4, 5]

c=a is my_list
d=b is not my_list

# Membership operators
element_in_list = 3 in my_list
element_not_in_list = 5 not in my_list

print("a is my_list:", c)
print("b is not my_list:", d)
print("3 in my_list:", element_in_list)
print("6 not in my_list:", element_not_in_list)