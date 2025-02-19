def reverseString_pythonic(s: List[str]) -> None:
    """
        More like, solve the problem in pythonic way.
        Using the `~i` function in python.
    """
    for i in range(len(s) // 2):
        s[i], s[~i] = s[~i], s[i]