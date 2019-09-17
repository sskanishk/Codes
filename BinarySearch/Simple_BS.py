# Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False
# print(linear_search(data, 12))


# Binary Search Iterative Method

def BS_Iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


# Recursive Approach

# keep the low after high --> if (...., high, low) ---> wrong answer --> Dont change order
def BS_Rec(data, target, low, high):
    # Base condition(search space is exhausted)
    if low > high:
        return False
    else:
        # we find the mid value in the search space and compares it with target value
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return BS_Rec(data, target, low, mid - 1)
        else:
            return BS_Rec(data, target, mid + 1, high)



data = [1,12,23,34,45,46,57,68,79,80,81,88,93,104,105,111,117,128,129,130]
target = 111

print(BS_Rec(data, target, 0, len(data)-1))
print(BS_Iterative(data, target))

