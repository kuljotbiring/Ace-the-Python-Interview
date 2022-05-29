# a set is an unordered collection of data items
# sets are not indexed, so we cannot use indices or the get() function
# similar to a bag in C
# cannot add mutable data structures like dictionaries or lists to a set
# a set does not allow duplicates
# a set is a good way to track the existence of items

# creating a set
random_set = {"Educative", 1408, 3.142,
              (True, False)}
print(random_set)
print(len(random_set))  # Length of the set

# create a set using the set constructor
empty_set = set()
print(empty_set)

random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)


# add items to a set
# for single items we can use the add() method
# for multiple items we can use the update() method
empty_set = set()
print(empty_set)

empty_set.add(1)
print(empty_set)

empty_set.update([2, 3, 4, 5, 6])
print(empty_set)

# remove items from a set using remove() or discard()
# remove() will generate an error if the item is not found
# discard() will not generate an error()
random_set = set({"Educative", 1408, 3.142, (True, False)})
print(random_set)

random_set.discard(1408)
print(random_set)

random_set.remove((True, False))
print(random_set)

# iterate over a set - we can use a for loop (since elements unordered - picks elements randomly)
odd_list = [1, 3, 5, 7]
unordered_set = {9, 10, 11, 12, 13, 14, 15, 16, 17}

print(unordered_set)

for num in unordered_set:
    if not num % 2 == 0:
        odd_list.append(num)

print(odd_list)
