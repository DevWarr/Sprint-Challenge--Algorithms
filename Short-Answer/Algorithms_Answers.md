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

There are two ways the I first think of to find the floor where eggs first start breaking. We can safely say:
    -   The building has floors numbered numerically
    -   There is no 'gradual breaking'. In other words, etiher the eggs don't break, or they all break (boolean values instead of weighted values)
    
    -   We could have our building like an array:
        -   [False, False, False, False, False, True, True, True]
    -   We're looking for the _one specific floor_ where the eggs will break, but one floor down the eggs won't break

The first way to search would be linear:
    -   Start at the top of the buiding, and check: Will eggs break? 
    -   If the eggs will break, then will they break one floor down?
    -   If the eggs break on our current floor _and_ they break one floor down, we're too high.
    -   If the eggs break on our current floor, but they _don't break_ one floor down, we've found our floor.
    - Time Complexity: O(n)

The second way to search would be binary:
    -   Our building is numerically floored, so it's considered sorted.
    -   Look at the half way point in the building: Will eggs break?
    -   If the eggs will break, then will they break one floor down?
        -   If the eggs break on our current floor _and they break one floor down,_ we're too high. Take the lower half of the list and search again.
    -   If the eggs will not break, when will they break one floor up?
        -   If the eggs don't break on our current floor _and they don't break one floor up,_ we're too low. Take the upper half of the list and search again.
    -   Once we find a pair where the lower floor doesn't break eggs and one floor up does break eggs, we can return the floor that does break eggs as our answer.
    - Time Complexity: O(log(n))