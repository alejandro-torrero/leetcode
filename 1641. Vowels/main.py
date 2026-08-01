# Parameters:
#  n: int

# Return type: int


def count(n, lastLetter="", lookup=None):
    lookup = {} if lookup is None else lookup

    if (n, lastLetter) in lookup:
        return lookup[(n, lastLetter)]

    if n == 0:
        return 1

    nb = 0

    for vowel in ["a", "e", "i", "o", "u"]:
        if lastLetter <= vowel:
            nb += count(n - 1, vowel, lookup)

    lookup[(n, lastLetter)] = nb
    return lookup[(n, lastLetter)]


print(count(4))
