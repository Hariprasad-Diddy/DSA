# Product of Digits

## Problem
Given an integer n, calculate the product of its digits.
The function should handle both positive and negative numbers.

## Examples
Input: 123
Output: 6
Explanation: 1 × 2 × 3 = 6

Input: -456
Output: 120
Explanation: 4 × 5 × 6 = 120

Input: 105
Output: 0
Explanation: 1 × 0 × 5 = 0

Input: 0
Output: 0

# Approach
* If the number is 0, return 0 (since the only digit is 0).
* Convert the number to its absolute value to ignore the sign.
* Initialize a variable product = 1.
* Extract each digit using number % 10.
* Multiply the digit with product.
* Remove the last digit using number //= 10.
* Repeat until the number becomes 0.
* Return the final product.

# Complexity Analysis
Let d be the number of digits in the number.

## Time Complexity: O(d)
Since each digit is processed exactly once.
Because the number of digits in n is approximately log₁₀(n), we can also write:
O(log n)

## Space Complexity: O(1)
Only a constant amount of extra space is used.

## Edge Cases Covered
* Negative numbers (sign ignored)
* Number = 0
* Numbers containing zero digits
* Large integers
