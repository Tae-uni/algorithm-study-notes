def arrayPairSum(nums: List[int]) -> int:
    total = 0
    pair = []
    nums.sort()

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            total += min(pair)
            pair = []

    return total