# 
class Solution:
    # fuction 1 for [left, right] 
    def search_fc1(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1
    # fuction 2 for [left, right)
    def search_fc2(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                return middle
        return -1
#
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_solu = Solution()
test_res1 = test_solu.search_fc1(arr, 5)
test_res2 = test_solu.search_fc1(arr, 5)
print(f'The result of fun1 is {test_res1}')
print(f'The result of fun2 is {test_res2}')

