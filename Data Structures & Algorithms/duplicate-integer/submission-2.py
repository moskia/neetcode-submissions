class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniqElem = set()
        for num in nums: 
            if num in uniqElem:
                return True
            uniqElem.add(num)
        return False
        