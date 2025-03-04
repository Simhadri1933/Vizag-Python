def find_non_repeating(arr):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    
    non_repeating = [x for x in arr if counts[x] == 1]
    return non_repeating

# Example usage
arr = [1, 2, 2, 3, 4, 4, 5]
result = find_non_repeating(arr)
print(result)