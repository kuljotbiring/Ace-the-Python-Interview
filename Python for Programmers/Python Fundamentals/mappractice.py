"""
The built-in map() function creates a map object using an existing list and a function as its parameters. This object
can be converted to a list using the list() function (more on this later).

The template for map() is as follows:

map(function, list)
"""
# The function will be applied, or mapped, to all the elements of the list.
num_list = [0, 1, 2, 3, 4, 5]

# double_list is a newly created list
double_list = map(lambda n: n * 2, num_list)

print(list(double_list))
