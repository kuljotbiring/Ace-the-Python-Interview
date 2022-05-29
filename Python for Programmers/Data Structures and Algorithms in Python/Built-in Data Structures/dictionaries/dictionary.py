# A dictionary stores key-value pairs, where each unique key is an index which holds the value associated with it.
# dictionary is an unordered data structure, the order of the output will not necessarily match the order in which we
# wrote the entries. Key-value pairs are accessed in a random or unordered manner.

# creating a dictionary
empty_dict = {}  # Empty dictionary
print(empty_dict)

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

# creating a dictionary using the dict() constructor
empty_dict = dict()  # Empty dictionary
print(empty_dict)

phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)])
print(phone_book)

# how to access dictionary values. you can use a key or the .get() method
phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book["Cersei"])
print(phone_book.get("Ghostbusters"))

