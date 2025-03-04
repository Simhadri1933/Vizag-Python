def search_element(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element
    return -1
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 91
print(search_element(arr, target))