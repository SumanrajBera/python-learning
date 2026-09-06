# LOOPs
- Loops are ued for performing repetitive task.

# for-loop

## for-in loop
- Here we can use arrays or strings any iterable and use them.
```py
nums = [1,2,3,4]
for x in nums:
    print(x)
```

## for loop with range
- `range` function can be used for iteration from custom start to end with steps
- It has 3 parameters:
  - startIdx: From where to start *(default is 0)*
  - endIdx: Where to end *(Its always endIdx + 1)*
  - steps: How the jump can both in +ve and -ve direction
```py
# From 0 to 11 will print 
for i in range(0,12,1):
    print(i)
```

## for-else loop
- Here we have a if statement with break in for loop and else immpediately after for-loop. So it excutes for-loop and if the break in if-statement executes then else-statement won't execute. And if the break doesn't execute then else will execute after the for loop completes
```py
# The else won't execute as the break hits.
for i in range(0,12,1):
    if i % 2 != 0:
        break
else:
    print("They are all even numbers")
```