# def findMedian(arr):
#     n = len(arr)
    
#     # First we sort the array
#     arr.sort()

#     # check for even case
#     if n % 2 != 0:
#         return arr[n // 2]

#     return (arr[(n - 1) // 2] + arr[n // 2]) / 2.0

# arr = [1, 3, 4, 2, 7, 5, 8, 6]
# ans = findMedian(arr)
# print(ans)
# Define a function to calculate the median of a list of numbers
def cal_median(nums):
    nums.sort()
    n = len(nums)
    m = n // 2
    
    if n % 2 == 0:
        return (nums[m-1]+nums[m]) / 2
    else:
        return nums[m]

# Test cases
print(cal_median([1,2,3,4,5]))
print(cal_median([1,2,3,4,5,6]))
print(cal_median([6,1,2,4,5,3]))
print(cal_median([1.0,2.11,3.3,4.2,5.22,6.55]))
print(cal_median([1.0,2.11,3.3,4.2,5.22]))
print(cal_median([2.0,12.11,22.3,24.12,55.22]))

