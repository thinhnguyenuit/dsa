import random
import array


def bubble_sort(arr: list) -> list:
    """
    Sort a list to non-decreasing order using bubble sort
    :param arr: list
    :return: sorted list
    """
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    random.seed(10)
    random_arr = [random.randint(1, 1000) for _ in range(50)]
    sorted_arr = bubble_sort(random_arr.copy())
    print(random_arr)
    print(sorted_arr)
