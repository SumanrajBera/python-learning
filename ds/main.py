import copy

a = [10,[20,80]]

refCopy = a
shallowCopy = a.copy()
deepCopy = copy.deepcopy(a)

refCopy[0] = 80
print("Original:", a)
print("Reference Copy Change:", a)

# Here change happens only in shallow copy
shallowCopy[0] = 5
print("Original:", a)
print("Shallow Copy changes 1 level deep:",shallowCopy)

# Here change happens in both shallow copy and original
shallowCopy[1][0] = 40
print("Original:", a)
print("Shallow Copy changes 2 level deep:",shallowCopy)

# Here changes only happen in deep copy
deepCopy[0] = 10
print("Original:", a)
print("Deep Copy changes 1 level deep:",deepCopy)
deepCopy[1][0] = 90
print("Original:", a)
print("Deep Copy changes 2 level deep:",deepCopy)