def sequence_search(arr: list, k: int) -> int:
    """
    Search item is in a list or not using sequence search
    :param arr: list
    :param k: item to search for
    :return: index of item if it exists in arr or -1 if not
    """
    n = len(arr)
    arr.append(k)
    i = 0
    while arr[i] != k:
        i += 1
    if i < n:
        return i
    else:
        return -1


if __name__ == "__main__":
    base_arr = [12, 45, 67, 13, 20, 112]
    idx = sequence_search(base_arr, 21)
    print(idx)
