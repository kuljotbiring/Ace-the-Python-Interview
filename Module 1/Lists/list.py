l = [1, 2, 3, 4, 5]
print(l)  # prints the entire list
print(l[0])  # prints value at index 0
print(l[1])  # prints value at index 1

# sublist use index slicing list[startindex:endindex]
# the startindex is inclusive and endindex is exclusive

list = ['a', 'b', 'c', 'd', 'e']

# use a substring to print a, b, c
print(list[0:3])
# use a substring to print d, e
print(list[3:5])

# Lists can be concatenated using the + operator
list_1 = [1, 2]
list_2 = [3, 4]
# will print [1, 2, 3, 4]
print(list_1 + list_2)

# traverse a list using for loop
my_list = [1, 2, 4, 8, 10]

for val in my_list:
    print(val)


