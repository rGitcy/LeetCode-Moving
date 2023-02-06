# change the value of array according to index
def change(nums, val, i):
    if 0<= i <=len(nums)-1:
        nums[i] = val
#
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
i, val = 2, 11
change(arr, val, i)
print(arr)