import random


def merge_sort(arr):
    """
    implement merge sort algorithms
    :param arr: array need to be sorted
    :return: sorted array in nondecreasing order
    """
    n = len(arr)
    if n < 2:
        return arr

    mid = int(n / 2 + 0.5)
    left = arr[0:mid]
    right = arr[mid:]
    s_left = merge_sort(left)
    s_right = merge_sort(right)
    return merge(s_left, s_right)


def merge(arr_a, arr_b):
    i = 0
    j = 0
    arr = []
    while i < len(arr_a) and j < len(arr_b):
        if arr_a[i] <= arr_b[j]:
            arr.append(arr_a[i])
            i += 1
        else:
            arr.append(arr_b[j])
            j += 1
    if i == len(arr_a):
        arr.extend(arr_b[j:])
    else:
        arr.extend(arr_a[i:])
    return arr


if __name__ == "__main__":
    random.seed(10)
    random_arr = [random.randint(1, 1000) for _ in range(20)]
    sort_arr = merge_sort(random_arr)
    print(random_arr, '\n', sort_arr)
