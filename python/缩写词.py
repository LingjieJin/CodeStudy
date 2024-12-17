def acronym(phrase):
    words = phrase.split()
    res = ""
    for word in words:
        res = res + word[0].upper()
    return res

