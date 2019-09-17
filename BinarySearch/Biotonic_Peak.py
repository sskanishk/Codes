# 1 2 3 4 5 4 3 2 1 ---> peak element = 5
# 1 2 3 4 1         ---> peak element = 4
# 1 6 5 4 3 2 1     ---> peak element = 6

def peak_element(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2

        mid = (low + high) // 2

        mid_left = A[mid - 1] if mid - 1 > 0 else float("inf")
        mid_right = A[mid + 1] if mid + 1 < len(A) else float("inf")

        if mid_left < A[mid] and mid_right > A[mid]:
            low = mid + 1
        elif mid_left > A[mid] and mid_right < A[mid]:
            high = mid - 1
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]
        else:
            return None

        # if A[mid] < A[mid + 1] and A[mid] > A[mid - 1]:
        #     low = mid + 1
        # elif A[mid] > A[mid + 1] and A[mid] < A[mid - 1]:
        #     high = mid - 1
        # else:
        #     return A[mid]

        # if A[mid] > A[mid + 1] and A[mid] > A[mid - 1]:
        #     if A[mid + 1] == A[mid - 1]:
        #         return A[mid]
        #     else:
        #         if A[mid] < A[mid + 1] and A[mid] > A[mid - 1]:
        #             low = mid + 1
        #         elif A[mid] > A[mid + 1] and A[mid] < A[mid - 1]:
        #             high = mid - 1
        #         else:
        #             return A[mid]
        # return None

# A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# A = [1, 2, 3, 4, 1]
# A =[8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]
# A = [1, 3, 50, 10, 9, 7, 6]
A =[10, 20, 30, 40, 50]
# A = [1, 6, 5, 4, 3, 2, 1]
print(peak_element(A))