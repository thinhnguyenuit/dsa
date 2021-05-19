import selection_sort
import random

if __name__ == "__main__":
    random.seed(10)
    random_arr = [random.randint(1, 1000) for _ in range(50)]
    sorted_arr = selection_sort.selection_sort(random_arr.copy())
    print(random_arr)
    print(sorted_arr)
