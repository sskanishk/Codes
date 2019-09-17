# A[i] == i  this is called fixed point in array

# Linear Approach
# Time Complexity O(n)
# Space Complexity O(1)
# def linaer(A):
#     for i in range(len(A)):
#         if A[i] == i:
#             return A[i]
#         else:
#             return None


def find_fixed_point(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]
    return None

# A = [-10, -5, 0 , 3, 7]
A = [0, 2, 5, 8, 17]
# A = [-10, -5, 3, 4, 7 , 9]

x = find_fixed_point(A)
print(x)