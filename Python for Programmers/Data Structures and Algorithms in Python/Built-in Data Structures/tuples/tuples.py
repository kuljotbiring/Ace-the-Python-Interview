# Tuples are similar to lists except they are immutable. Since tuples are immutable, we can’t add or delete elements
# from them. Furthermore, it isn’t possible to append another tuple to an existing tuple.

car = ("Ford", "Raptor", 2019, "Red")
print(car)

# Length
print(len(car))

# Indexing
print(car[1])

# Slicing
print(car[2:])

# you can merge tuples with the + operator
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = hero1 + hero2
print(awesome_team)

# like lists, tuples can be nested
hero1 = ("Batman", "Bruce Wayne")
hero2 = ("Wonder Woman", "Diana Prince")
awesome_team = (hero1, hero2)
print(awesome_team)

# we can search for an element in a tuple using the in operator
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Moscow" in cities)

# using index function can give us index of a value in a tuple
cities = ("London", "Paris", "Los Angeles", "Tokyo")
print(cities.index("Tokyo"))
