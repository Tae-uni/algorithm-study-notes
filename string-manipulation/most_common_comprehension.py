def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    """
    Using List Comprehension, filtered with regular expressions.
    List Comprehension is a concise way to create lists in Python.
    Faster and more readable compared to using loops.
    """
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
             if word not in banned]

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]