def selection_sort(arr: list) -> list:
    """
    Sort a list to non-decreasing order using selection sort
    :param arr: random list or array
    :return: sorted list
    """
    n = len(arr)
    min_item = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[j] < arr[min_item]:
                min_item = j
        arr[i], arr[min_item] = arr[min_item], arr[i]
    return arr
