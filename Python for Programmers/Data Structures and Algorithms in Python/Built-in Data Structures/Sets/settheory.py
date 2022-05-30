# unions
# A union of two sets is the collection of all unique elements from both sets.
# since sets are unordered output will be random
# union can be performed using either the pipe operator, |, or the union() method:
set_A = {1, 2, 3, 4}
set_B = {'a', 'b', 'c', 'd'}

print(set_A | set_B)
print(set_A.union(set_B))
print(set_B.union(set_A))


# intersection
# intersection of two sets is the collection of unique elements which are common between them.
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}

print(set_A & set_B)
print(set_A.intersection(set_B))
print(set_B.intersection(set_A))


# difference
# difference between two sets is the collection of all unique elements present in the first set but not in the second.
# set_A - set_B returns the elements which are only present in set_A.
# set_B - set_A would do the opposite.
set_A = {1, 2, 3, 4}
set_B = {2, 8, 4, 16}


print(set_A - set_B)
print(set_A.difference(set_B))

print(set_B - set_A)
print(set_B.difference(set_A))

