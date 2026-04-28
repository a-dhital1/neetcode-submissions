class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        empty_list = []
        for i in nums:
            if i in empty_list:
                return True
            else:
                empty_list.append(i)
        return False