myDict = {
    "fast": "In a Quick Manner",
    "shayan": "A Coder",
    "marks": [1,2,5],
    "anotherdict": {'Shayan': 'Player'},
    1:2
}

#Dictionary Methods

print(list(myDict.keys())) # Prints the keys of the dictonary
print(myDict.values()) # Prints the key of the dictionary
print(myDict.items()) #Prints the (key, value) for all contents of the dictionary
print(myDict)
updateDict = {
    "Lovish": "Friend",
    "Yash": "Friend",
    "Mihir": "Friend"
}

myDict.update(updateDict) #Updates the dictionary by adding the key values pairs of the dictionary
print(myDict)

print(myDict.get("shayan"))