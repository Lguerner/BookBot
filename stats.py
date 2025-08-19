def get_num_words(f):
    array = f.split()
    return len(array)


def get_num_symblos(f):
    dic_symblos = {}
    for word in f:
        lowered = word.lower()
        if lowered in dic_symblos:
            dic_symblos[lowered] += 1
        else:
            dic_symblos[lowered] = 1
    return dic_symblos
