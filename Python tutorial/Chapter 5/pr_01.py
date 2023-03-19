myDict = {
    "Panka": "Fan",
    "Dabba": "Box",
    "Vastu": "Thing"    
}

print("Options are", myDict.keys())
a = input("Enter the Hindi word\n")

#Below line will not throw an error if the key is not present
# in the dictionary
print("The meaning of your word is:", myDict.get[a])