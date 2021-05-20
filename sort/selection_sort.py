import random


def selection_sort(arr: list) -> list:
    """
    Sort a list to non-decreasing order using selection sort
    :param arr: random list or array
    :return: sorted list
    """
    n = len(arr)
    for i in range(n):
        min_item = i
        for j in range(i+1, n):
            if arr[j] < arr[min_item]:
                min_item = j
        arr[i], arr[min_item] = arr[min_item], arr[i]
    return arr


if __name__ == "__main__":
    random.seed(10)
    random_arr = [random.randint(1, 1000) for _ in range(50)]
    sorted_arr = selection_sort(random_arr.copy())
    print(random_arr)
    print(sorted_arr)
