# Persistence

Additive Persistence

The additive persistence of an integer, n, is the number of times you have to replace n with the sum of its digits until n becomes a single digit integer.

Create a function that take an integer as an argument and returns its additive persistence.

Examples: Additive Persistence

additive_persistence(1679583) ➞ 3
# 1 + 6 + 7 + 9 + 5 + 8 + 3 = 39
# 3 + 9 = 12
# 1 + 2 = 3
# It takes 3 iterations to reach a single-digit number.

additive_persistence(123456) ➞ 2
# 1 + 2 + 3 + 4 + 5 + 6 = 21
# 2 + 1 = 3

additive_persistence(6) ➞ 0
# Because 6 is already a single-digit integer.
