import random


def insertion_sort(arr: list) -> list:
    n = len(arr)
    for i in range(1, n-1):
        v = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > v:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = v

    return arr


if __name__ == "__main__":
    random.seed(10)
    random_arr = [random.randint(1, 1000) for _ in range(50)]
    sorted_arr = insertion_sort(random_arr.copy())
    print(random_arr)
    print(sorted_arr)
