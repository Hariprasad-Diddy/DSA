# Count Digits in a Number

## Problem
Given an integer `n`, count the number of digits present in it.

## Example
input = 12345
output = 5

input = 1
output = 1

input = 0
output = 1

## Approach
Repeatedly divide the number by 10 until it becomes 0.

## Code
📄 [count_digits.py](./count_digits.py)

## Complexity
- Time: O(log n)
- Space: O(1)
