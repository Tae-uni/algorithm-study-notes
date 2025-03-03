def arrayPairSum(nums: List[int]) -> int:
    total = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            total += n

    return total