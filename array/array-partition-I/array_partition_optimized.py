def arrayPairSum(nums: List[int]) -> int:
    nums.sort()

    return sum(nums[::2])