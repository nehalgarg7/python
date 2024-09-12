# tuple is a data type that lets us create immutable sequence of values.

tup = (1,2,3,4)

## tup[0] = 46      not allowed in python

tup1 = ()
print(tup1, type(tup1))


tup2 = (1) #python consider this a integer and type will be <class'integer'>
tup3 = (1,) #now python consider this a tuple.

##methods

"""
tup = (2,1,3,1)

tup.index(ele) #returns index of first occurence
tup.count(ele) #counts total occurrences

"""