# create new dictionary.
phone_book = {"John": 123, "Jane": 234, "Jerard": 345}    # "John", "Jane" and "Jerard" are keys and numbers are values
print(phone_book)

# Add new item to the dictionary
phone_book["Jill"] = 345
print(phone_book)

# Remove key-value pair from phone_book
del phone_book ["John"]

#Print Jane's phone number from phone_book .
#Hint : Use dict indexing e.g. dct[key]
pass
print(phone_book["Jane"])