#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

This would have a time complexity of O(n).
We have a loop with a max of n^3, but each iteration is adding n^2.

For example:
```py
a = 0
while (a < n * n * n):
    a = a + n * n

# If n = 5:
a = 0
while (a < 125):
    a = a + 25
# Loop 1:  
#          a = 0;  0 < 125 => True
#          a = 0 + 25 = 25
# Loop 2:
#          a = 25;  25 < 125 => True
#          a = 25 + 25 = 50
# Loop 3:
#          a = 50;  50 < 125 => True
#          a = 50 + 25 = 75
# Loop 4:
#          a = 75;  75 < 125 => True
#          a = 75 + 25 = 100
# Loop 5:
#          a = 100;  100 < 125 => True
#          a = 100 + 25 = 125
# 
# Loop 6:
#          a = 125; 125 < 125 => False
#          break
# 
```
Even with n multiplied by itself, if n = 5 we still loop only 5 times. Time complexity: O(n)


b) 

This would have a time complexity of O(nlog(n)).
    -   We have one loop moving linearly (time of O(n))
    -   We have a nested loop doubling up until n (time of O(log(n)))
    - Because these loops are nested, we multiply their time complexities ( O(n) * O(log(n)) = O(nlog(n)) )
Time Complexity: O(nlog(n))

c)
This would haev a time complexity of O(n).
    -   This recursion is acting as a loop, decreaing n linearly until it hits 0
    -   Fun fact: This would also have a space complexity of O(n) because each recursive call would add to the call stack.

You could write the same function like this for O(1) space complexity:
```python
def bunnyEars(bunnies):
    ears = 0
    for i in range(bunnies):
        ears += 2
    return ears
```

AND, because this function assumes all bunnies have 2 ears,you could just type this for O(1) time complexity:
```python
def bunnEars(bunnies):
    return 2 * bunnies
```

## Exercise II


