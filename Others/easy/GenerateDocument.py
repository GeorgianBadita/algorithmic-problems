def generateDocument(characters, document):
    count_chars = {}
    for char in characters:
        count_chars[char] = count_chars.get(char, 0) + 1

    count_doc = {}
    for char in document:
        count_doc[char] = count_doc.get(char, 0) + 1

    for char in count_doc:
        if char not in count_chars or count_doc[char] > count_chars[char]:
            return False
    return True
