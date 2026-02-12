# Check Prime Number

## Problem
Given an integer `n`, determine whether it is a prime number.

A prime number is a number greater than 1 that has exactly two distinct positive divisors: 1 and itself.

---

## Examples
Input:  n = 7
Output: True

Input:  n = 10
Output: False

Input:  n = 1
Output: False

## Approach

A number `n` is prime if:

- It is greater than 1
- It has no divisors other than 1 and itself

### Optimization Strategy

Instead of checking all numbers from `2` to `n-1`, we:

1. Eliminate numbers ≤ 1
2. Handle `2` separately
3. Eliminate even numbers
4. Check divisibility only up to √n
5. Skip even divisors

Why only up to √n?

If `n = a × b`, then at least one of `a` or `b` must be ≤ √n.

---

## Python Implementation

📄 **Source Code:**  
👉 [prime_check.py](./prime_check.py)
