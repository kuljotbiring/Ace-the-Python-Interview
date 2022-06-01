# The dict() constructor cannot be used in the same way as the others because it requires key-value pairs instead of
# just values. Hence, the data must be stored in a format where pairs exist.
#
# For example, a list of tuples where the length of each tuple is 2 can be converted into a dictionary.
#
# Those pairs will then be converted into key-value pairs:
star_wars_list = [[1,"Anakin"], [2,"Darth Vader"], [3, 1000]]
print (star_wars_list)
star_wars_tup = ((1, "Anakin"), (2, "Darth Vader"), (3, 1000))
print (star_wars_tup)
star_wars_set = {(1, "Anakin"), (2, "Darth Vader"), (3, 1000)}
print (star_wars_set)

star_wars_dict = dict(star_wars_list) # Converting from list
print(star_wars_dict)

star_wars_dict = dict(star_wars_tup) # Converting from tuple
print(star_wars_dict)

star_wars_dict = dict(star_wars_set) # Converting from set
print(star_wars_dict)
