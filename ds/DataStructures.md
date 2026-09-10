# Data Structures
- Data structures are used to organise and manage data efficiently
- There are two type of data structures:
  - `In-built`: Tuples, list, etc.
  - `Customised`: Queue, stack, etc.

## List
- This is used to store multiple types of data type to store an ordered collection of items.
- It is `heterogenous` in nature which means it can store multiple types of data at the same time.
- It is `mutable` in nature.
- Here we can access the items of the list via indexing and it can be both positive and negative.
```py
li = [1,2,3,4]
print(li[0],li[-4]) # This prints the same item
```
- Here we also have slicing feature just like strings where we can slice based on `li[startIdx: stopIdx: step]`. `startIdx` is 0 by default. If we make `step` -1 then it will slice in reverse but we need to make sure startIdx is smaller than stopIdx. 

### Deep and shallow copy
- `Reference copy`: In this copy if we make changes in the copy it also makes changes in the original
- `Shallow copy`: In this copy if we make changes 1 level below the original then it will not reflect in original but after 1 level it will reflect in the original.
- `Deep copy`: In this copy it is a fully independent copy of the original.
```py
import copy
# How to make different copies
refCopy = a
shallowCopy = a.copy()
deepCopy = copy.deepcopy(a)
```

### List traversal
- We can traverse the entire list in the same way we do with string which are:
  - for-in loop
  - using range function

**Note**: We can use `help(list)` to get help with list.

### Commonly used function in list
- append(item): This is used to add item to the list
- clear(): This is used to clear all items.
- count(item): This can be used to count items of the list.
- insert(idx, item): This can be used to insert item at specific index
- pop(): It removes and returns at index = -1

## Tuples
- Tuples are also used multiple values and is also heterogenous in nature.
```py
# syntax
tup = (1,2,3,4)
```
- It is immutable in nature.
- Here the indexing, slicing and traversing are similar to list and string.
- We can make use of `tuple(list)` to make a list into a tuple.
- It has two helpful methods: `count(item)` and `index(item)`

### Tuple unpacking
- We can unpack tuples into variables
```py
a,b,c = (1,2,3)
print(a) # this will print 1

# but this causes one more problem suppose we have a tuple of only one value
a = (1)
print(type(a)) # this will be int as it unpacked it  
```
- To survive from single value tuple being unpacked always apply a comma

**Note**: Tuple and list both allow duplicate values

## Set
- Set can also be used to store multiple values which can be hashed. For ex: string, number, functions and boolean.
```py
# basic syntax to create set
s = {10,20}

# but if you create an empty set
s = {}
print(type(s)) # this will be a dictionary

# Hence to create an empty set we can set()
s = set()
print(type(s)) # this will be a set
```
- It has unordered nature.
- We cannot have duplicate values in set.
- We can use set() constructor to convert list into a set.
- It has a semi-mutable natue as we cannot edit the elements that are stored inside the set.

### Commonly used methods of set
- add(item): It adds an item to the set.
- remove(item): It removes an item from the set.
- clear(): It is used to clear all items from the set
- difference(): It returns a difference between the two sets which means that element that exist in first but not in second. Suppose a and b so `a.difference(b)` will give us elements that exist in set a but no in b. We can also use `-` for shorter usage *(a-b)*.
- discard(item): Does the same remove item from set but if element is not present fails silently
- -=: It can used for difference and assigning
- intersection() or `&`: It returns the common in both sets.
- &=: To find intersetion and assign.
- symmetric_difference() or `^`: It is used to return elements which are in either sets but not in both.
- |: It is used for return union of both sets.
- `>=`: It is used to return boolean if first set is superset of the other set.
- <=: It is used to return boolean if first set is subset of the other set.
**Note**: There are more useful methods which can be experimented with. *(w3school for reference)*

## Dictionary
- 
