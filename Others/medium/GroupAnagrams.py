def groupAnagrams(words):
    if not words:
        return []

    if len(words) == 1:
        return [words]

    words = [(sorted(word), word) for word in words]
    words = sorted(words, key=lambda x: x[0])

    anagrams = []
    current_anagram = [words[0][1]]
    for word_tuple in words[1:]:
        _, word = word_tuple
        if is_anagram(word, current_anagram[-1]):
            current_anagram.append(word)
        else:
            anagrams.append(current_anagram)
            current_anagram = [word]

    if len(current_anagram) > 0:
        anagrams.append(current_anagram)

    return anagrams


def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    freq1 = [0] * 26
    freq2 = [0] * 26
    for i in range(len(word1)):
        freq1[ord(word1[i]) - ord('a')] += 1
        freq2[ord(word2[i]) - ord('a')] += 1

    return freq1 == freq2


words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams(words))
