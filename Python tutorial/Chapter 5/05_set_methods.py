#Creating an empty set
b = set()
print(type(b)) 

#Adding values to an empty set
b.add(4)
b.add(5)
b.add((4, 5, 6))


# b.add({4, 5, 6}) # Cannot add dictionary in a set
print(b)

print(len(b)) # Prints the length of the set

#Removal of an item
b.remove(5) # Removes 5 from set b
# b.remove(15) # Throws an error while trying to remove 15(Which is not present in the set)
print(b)

print(b.pop()) 