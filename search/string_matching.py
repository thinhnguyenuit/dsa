def brute_force_string_matching(text: str, pattern: str) -> int:
    """
    String matching use brute force algorthms
    :param text: string of n character
    :param pattern: a pattern to search for
    :return: index of fisrt character of matching string in text or -1 otherwise
    """
    n = len(text)
    m = len(pattern)
    for i in range(n-m):
        j = 0
        while j < m and pattern[j] == text[j+i]:
            j += 1
        if j == m:
            return i
    return -1


if __name__ == "__main__":
    base_test = "hellopapneh"
    pat = "pap"
    idx = brute_force_string_matching(base_test, pat)
    print(idx)
