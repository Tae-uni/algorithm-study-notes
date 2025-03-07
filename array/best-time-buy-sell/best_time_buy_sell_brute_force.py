def maxProfix(prices: List[int]) -> int:
    max_price = 0

    # Optimized one.
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - prices[i], max_price)

    """Book, do not need to use enumerate for index and value in this case.
        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price, max_price)
    """

    return max_price