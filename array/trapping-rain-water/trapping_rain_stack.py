def trap(height: List[int]) -> int:
    """
        Using a Monotonic Decreasing Stack.
    """
    stack = []
    volume = 0

    for i in range(len(height)):
        # stack[-1] : The latest value.
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            # Width of trapped water
            distance = i - stack[-1] - 1

            # Height of trapped water
            water = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * water

        stack.append(i)
    return volume