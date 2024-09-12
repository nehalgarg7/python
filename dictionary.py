# dictionaries are used to store data values in key:value pairs
# they are unordered, mutable(changeable) & don't allow duplicate keys

dict = {
    "name" : "Nehal Garg",
    "cgpa" : "8.8",
    "marks" : [98,80,75],
}
dict["name"] = "jsdhs"
print(dict["name"])

hello = {
    "message" : "Hi! my name is Nehal Garg"
}

##methods

"""
dict.keys() return all keys
dict.values() return all values
dict.items() return all (key,val) pairs as tuple
dict.get("key") return all value according to key, if key not exists then return NONE
dict.update(newDict) insert the specified items to the dictionary

"""

dict.update(hello)

print(dict)

print(dict.get("name"))