def binary_search(arr, k):
    """
    Implement nonrecursive binary search
    :param arr: an array sorted in ascending order
    :param k: seach key K
    :return: an index of array element that is equal to k
    """
    l = 0
    r = len(arr) - 1
    while l <= r:
        m = (l+r) // 2
        if k == arr[m]:
            return m
        elif k < arr[m]:
            r = m - 1
        else:
            l = m + 1
    return -1


if __name__ == "__main__":
    a = [1, 3, 4, 6, 9, 11, 12, 34, 44, 50, 56, 111]
    i = binary_search(a, 12)
    print(i, a[i])
