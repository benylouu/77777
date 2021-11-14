def merge(*lists):
    result = []
    for l in lists:
        result += list(set(l))
    return sorted(result)


if __name__ == 'main':
    data = [4, 5, 1], [1, 3, 4], [2, 6]
    print(merge(*data))
