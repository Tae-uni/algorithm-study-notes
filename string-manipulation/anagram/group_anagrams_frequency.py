def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """
        More details about Frequency-based "Hashmap", I'm going to study chapter later on.
        For now, just remember this way is also good way to solve the problem.
    """
    anagram = collections.defaultdict(list)

    for word in strs:
        # Create a frequency count list for 26 letters (a-z)
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1

        anagram[tuple(count)].append(word)

    return list(anagram.values())