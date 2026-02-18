# Check Palindrome

## Problem
Given a value `n`, check whether it is a palindrome.

A palindrome is a value that reads the same forward and backward.

The input can be:
- an integer
- a string

---

## Examples
Input:  121
Output: True

Input:  -121
Output: False

Input:  “madam”
Output: True

Input:  “hello”
Output: False

## Approach

### Integer (Math-Based)
1. Negative numbers are not palindromes.
2. Reverse the number using modulo (`% 10`) and integer division (`// 10`).
3. Compare the reversed number with the original number.

This avoids converting the integer to a string.

---

### String (Two-Pointer Technique)
1. Use two pointers: one at the start and one at the end.
2. Compare characters at both pointers.
3. Move pointers inward until they cross.

This avoids creating extra strings and uses constant space.

---

## Python Implementation
**Source Code:**  
[palindrome_number.py](./palindrome_number.py)

---

## Complexity Analysis

| Input Type | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Integer | O(log n) | O(1) |
| String | O(n) | O(1) |

- For integers, each iteration removes one digit.
- For strings, each character is compared at most once.

---

## Edge Cases
- `0` is a palindrome
- Negative integers are not palindromes
- Single-character strings are palindromes
- Empty strings (if allowed) can be considered palindromes

---

## Interview Notes
- Math-based approach is preferred for integers
- Two-pointer technique is optimal for strings
- Avoid string reversal for integers unless explicitly allowed

---

⬅️ **Back to Math Section**  
👉 [Math - DSA Series](../README.md)
