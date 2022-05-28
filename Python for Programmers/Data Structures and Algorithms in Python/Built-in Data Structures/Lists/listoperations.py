# adding elements to a list
num_list = []  # Empty list
num_list.append(1)
num_list.append(2)
num_list.append(3)
print(num_list)

# to insert in a particular index use insert method
new_list = [1, 2, 3, 5, 6]
new_list.insert(3, 4)  # Inserting 4 at the 3rd index. 5 and 6 shifted ahead
print(new_list)

# remove the last element from a list using pop
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
last_house = houses.pop()
print(last_house)
print(houses)

# remove element from specific location using the remove method
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
print(houses)
houses.remove("Ravenclaw")
print(houses)

# using remove on a nested list
populations = [["Winterfell", 10000], ["King's Landing", 50000],
               ["Iron Islands", 5000]]
print(populations)
populations.remove(["King's Landing", 50000])
print(populations)

# list slicing is used to get a portion of the list - the second number is non-inclusive
slice_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(slice_list[2:5])
# leaving the one of the arguments empty means end - the third argument can be used to skip ahead
print(slice_list[0::2])
# reverse a list
print(slice_list[::-1])

# use index method to find the index of a list item
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print(cities.index("Los Angeles"))  # It is at the 2nd index

# if we only want to verify if the item is in the list we can use in
cities = ["London", "Paris", "Los Angeles", "Beirut"]
print("London" in cities)
print("Moscow" not in cities)

# we can sort a list by using the sort function - alters the list
number_list = [20, 40, 10, 50.4, 30, 100, 5]
number_list.sort()
print(number_list)
