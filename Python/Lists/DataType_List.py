
listnum = [6,5,4,3,2,4,5,2]

#Add 11 at the end
listnum.append(11)

# Add 11 in position 0
listnum.insert(0,11)

listnum.sort()

# Reverse a list
reversed_list_num = list.reverse(listnum)

# Slicing:
# [start slice: end slice: step

# Slice excluding last element
listnum[:-1]

# Slice excluding last two elements
listnum[:-2]

#Reverse a list or traverse from the end with step 1
list[::-1]

#Reverse a list or traverse from the end with step 2
list[::-2]


#Traverse from the beginning with step 2
list[::2]

# Elements from index 1 (included) to the end (-1) excluded
list[1:-1]

# Shallow copy (another reference to the original list)
listnum[:]

# Element index 0 and 1 (2 is excluded)
listnum[0:2]

# Another list
listchar = ['b','g','h', 'o', 'o']

# Remove the first occurrence of 'o'
listchar.remove('o')

#Remove the second element starting from the end
listchar.pop(-2)