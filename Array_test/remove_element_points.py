# remove the element from array according to value via fast&slow points
class Solution:
    def remove(self, nums, val):
        fast, slow = 0, 0
        while fast < len(nums):
            if nums[fast]!=val:
                nums[slow] = nums[fast]
                slow += 1
            fast +=1
        return slow
test_solu = Solution()
arr = [1, 2, 3, 3, 4, 5, 6]
res = test_solu.remove(arr, 3)
print(res)