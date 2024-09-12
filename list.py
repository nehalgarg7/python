#list is a heterogenous array

marks = [1,2,3,4,5]
print(marks, type(marks), marks[0])

# len(marks)

marks[0] = 4 #we can mainpulate the list using indexing. (list are mutable)

print(marks)

#slicing : same as of string

## Methods
"""
list.append()
list.sort()
list.sort(reverse=True)
list.reverse()
list.insert(idx,ele)
list.remove(ele) #remove first occurrence of element
list.pop(idx) #remove element at idx
"""