# search a element from array according to a vakue given.
def search(nums, val):
    for i in range(len(nums)):
        if nums[i] == val:
            return i
    return -1
#
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
match_index = search(arr, 3)
print(f'the index of matched element is {match_index}')
