def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    words = re.findall(r'\w+', paragraph.lower())

    banned_set = set(banned)
    word_counts = collections.Counter(w for w in words if w not in banned_set)

    return word_counts.most_common(1)[0][0]