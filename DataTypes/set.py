# set is the collection of the unordered items(heterogenous). Each element in the set must be unique and immutable
# In set, repeated element is stored only once.

# immutable values like tuple, etc.can be added to set but mutuable values like lists can not be added to set because we cannot create a fixed hash value for it.


nums = {1,2,3,4,4,3,1,4,2}

print(nums)

null_Set = set() #empty set syntax

#len function to count the length

##methods
"""
set.add(ele)
set.remove(ele)
set.clear()
set.pop() removes a random value

set.union(set2)
set.intersection(set2)
"""

null_Set.add(1)
null_Set.add(2)

print(null_Set)