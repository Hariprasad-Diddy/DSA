# Reverse a Number

## Problem
Given an integer `n`, reverse its digits and return the reversed number.

### Example
Input:  n = 1234
Output: 4321

Input:  n = -120
Output: -21

## Approach
1. Extract the last digit using `n % 10`
2. Append the digit to the reversed number
3. Remove the last digit using integer division (`n // 10`)
4. Repeat until the number becomes `0`

Negative numbers are handled by reversing the absolute value and restoring the sign.

---

## Python Implementation
[reverse_number.py](./reverse_number.py)

---

## Complexity
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

---

## Edge Cases
- `n = 0` → output is `0`
- Negative numbers
- Trailing zeros (e.g., `120 → 21`)

---

## Interview Notes
- Each iteration removes one digit from the number
- Since the number is divided by 10 each time, the algorithm runs in logarithmic time

---

⬅️ **Back to Math Section:**  
👉 [Math - DSA Series](../README.md)
