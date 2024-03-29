# You are given a number N from 1 to 109.
# You want to form the number N as a sum of positive numbers ending with 9. For example: 28 = 19 + 9.
# Find the minimum number of summands (terms ending with 9) to achieve the task. Print -1 if impossible.

# Input:
# The first line of input contains a single integer T, denoting the number of testcases.
# The next T lines contain a single integer N each.

# Output:
# Print the minimum number of summands required to get N, or print -1 if impossible.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 109

# Sample Input
# 3
# 7
# 209
# 27

# Sample Output
# -1
# 1
# 3

# Sample Explanation
# - It is impossible to form 7 using positive integers ending with 9
# - 209 itself ends with 9, so it can be used as a solo term
# - 27 = 9 + 9 + 9, so minimum number of terms required is 3.


x = int(input())
y = []
for i in range(x):
    y.append(int(input()))

for i in range(x):
    if y[i] > 9:
        temp = 10 - (y[i]%10)
        if (y[i]-(temp * 9) >= 0):
            print(temp)
        else:
            print(-1)
    else:
        print(-1)