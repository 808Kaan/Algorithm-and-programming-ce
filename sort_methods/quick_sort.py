def quick_sort(values):
    if len(values) <= 1:
        return values

    pivot = values[len(values) // 2]

    left = [x for x in values if x < pivot]
    middle = [x for x in values if x == pivot]
    right = [x for x in values if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    my_list = [1, 3, 2, 7, 4, 12, 11]
    print(quick_sort(my_list))