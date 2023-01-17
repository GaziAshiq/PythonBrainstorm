def binary_search(li, y):
    left, right = 0, len(li) - 1
    while left <= right:
        mid = (left + right) // 2  # for integer division
        if li[mid] == y:
            return mid
        elif li[mid] < y:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 18, 20]

    for x in range(1, 22):
        position = binary_search(L, x)

        if position == -1:
            if x in L:
                print(x, 'is in List, but function returned -1')
            else:
                print(x, "not in list")
        else:
            if L[position] == x:
                print(x, 'found in correct position')
            else:
                print('binary search returned', position, 'for', x, 'which is incorrect')
    print('program end')
