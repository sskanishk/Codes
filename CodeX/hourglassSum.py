# Maximum hourglassSum
arr = []
for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

sum = []
for i in range(len(arr) - 2):
    for j in range(len(arr)-2):
        sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
print("Maximum Sum is",max(sum))

# 1 2 3 4 5 6
# 0 1 0 1 0 1
# 1 0 0 0 0 0
# 0 0 0 0 0 0
# 1 1 1 1 1 0
# 0 0 0 0 0 0
# 15


# # import math
# # import os
# # import random
# # import re
# # import sys
# x = []
# arr_count = int(input())
# arr = list(map(int, input().rstrip().split()))
# x = reversed(arr)
# print(reversed(arr))
# print(x)
#
#
#
# # class array:
# #     def __init__(self):
# #         self.list = []
# #
# #     def reverseArray(self, n):
# #         return reversed(arr)
# #
# # arr = array()
# # arr_count = int(input())
# # arr = list(map(int, input().rstrip().split()))
# # res = arr.reverseArray()
# # print(arr)
# # # print(' '.join(map(str, res)))
