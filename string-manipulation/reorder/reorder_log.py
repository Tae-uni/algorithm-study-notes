def reorderLogFiles(logs: List[str]) -> List[str]:
    # More pythonic way to solve.
    def sorting_algorithm(log):
        left, right = log.split(" ", 1)

        if right[0].isdigit():
            return (1,) # Put the digit at the end.
        else:
            return (0, right, left)

    return sorted(logs, key=sorting_algorithm)