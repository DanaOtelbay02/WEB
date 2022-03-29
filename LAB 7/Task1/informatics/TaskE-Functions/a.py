def min(a, b, c, d):
    min_arr = [a, b, c, d]
    min_arr.sort()
    return min_arr[0]

nums = list(map(int, input().split()))
print(min(nums[0], nums[1], nums[2], nums[3]))