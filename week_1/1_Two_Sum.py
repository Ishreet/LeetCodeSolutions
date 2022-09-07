class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # lookup table with difference as key and pair as value
        hashmap = {}

        # iterate through all values
        for i in range(len(nums)):

            # if difference is in the hashmap, return the pair index and
            # current index
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]

            # otherwise add the difference between target and current number
            # as key and its pair index as its value
            else:
                hashmap[target - nums[i]] = i
