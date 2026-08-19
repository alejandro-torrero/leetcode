# Parameters:
#  s: str
#  words: List[str]

# Return type: bool


def word_break(s, words, i=0, lookup=None):
    lookup = {} if lookup is None else lookup
    if i in lookup:
        return lookup[i]

    if i == len(s):
        return True

    for word in words:
        if word == s[i : i + len(word)] and word_break(s, words, i + len(word),lookup):
            lookup[i] = True
            return True
    lookup[i] = False
    return False


print(word_break("leetcode", ["leet", "code"]))
