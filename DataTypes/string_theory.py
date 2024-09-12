# string is a datatype  that stores a sequence of characters.
 
# concat -> used + operator "Nehal" + " Garg"
# length -> len(str)
# indexing -> str[0] we can access the character using indexing but cannot mainpulate it.

# slicing str[starting index : ending index] {starting index is inducled but ending index is not}
""" str = "Nehal Garg"
    str[1:4]
    str[ : 4] is same as str[0:4]
    str[1: ] is same as str[1 : len(str)]"""

str = "Nehal Garg"
print(str[1: len(str)])

"""
    we can do backward counting in python
    print(str[-5:-1]) // counting start from backward. -5,-4,-3,-2,-1
"""

print(str[-5:-1])

# function

"""
str.endswith()
str.capitalize() // capitalize the first letter of string and return it. do not modify the original string.
str.replace(old,new) // useful.
str.find(word)
str.count("str1")
"""