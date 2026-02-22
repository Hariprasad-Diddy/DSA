# Count Trailing Zeros

## Problem

Given an integer `n`, count how many trailing zeros are present in the number.

Trailing zeros are the number of consecutive zeros at the end of the number.

## Examples

Input: 1200  
Output: 2  
Explanation: 1200 ends with two zeros.

Input: 100  
Output: 2

Input: 1050  
Output: 1

Input: 0  
Output: 1 (0 itself is considered to have one trailing zero)

Input: -9000  
Output: 3

## Approach

1. If `n` is 0, return 1 (special case).
2. Convert `n` to absolute value to ignore the sign.
3. Initialize `count = 0`.
4. While the last digit is 0 (`n % 10 == 0`):
   - Increment `count`
   - Remove the last digit (`n //= 10`)
5. Return `count`.

## Complexity Analysis
Let k be the number of trailing zeros.

### Time Complexity: O(k)
We only loop over the trailing zeros, not all digits.

### Space Complexity: O(1)
Only constant extra space is used.

## Edge Cases Covered
* n = 0
* Negative numbers
* Numbers with no trailing zeros
* Numbers with multiple trailing zeros
