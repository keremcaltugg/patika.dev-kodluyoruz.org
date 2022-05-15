# Insertion Sort 

[22,27,16,2,18,6] -> Insertion Sort

### 1. Steps for Insertion Sort

In this algorithm, an element of the array is taken and sorted one by one with the elements backwards, and in each order, if it is smaller than the next element, the element taken is replaced by the element in front of it and thrown back one by one.

[22,27,16,2,18,6] --> [16,22,27,2,18,6] --> [2,16,22,27,18,6] --> [2,16,18,22,27,6] --> [2,6,16,18,22,27]

### 2. Big'O Notation

O(n^2)

### 3. Time Complexity 

##### -Worst Case: 
0+1+2+3+4…..+n-1 = [n*(n-1)]/2 : n^2

##### -Average Case: 
Average of worst and best case, which equals to n^2 

##### -Best Case: 
n 

### 4. What case does the number 18 fall into after the array is sorted?

After the sorting is applied, the number 18 is included in "average case" where it is in the middle parts.

### Write the first 4 steps of [7,3,5,8,2,9,4,15.6] according to Insertion Sort.

|Step 1|7|3|5|8|2|9|4|15|6|
|------|-|-|-|-|-|-|-|- |-|

|Step 2|3|7|5|8|2|9|4|15|6|
|------|-|-|-|-|-|-|-|- |-|

|Step 3|3|5|7|8|2|9|4|15|6|
|------|-|-|-|-|-|-|-|- |-|

|Step 3|3|5|7|8|2|9|4|15|6|
|------|-|-|-|-|-|-|-|- |-|
