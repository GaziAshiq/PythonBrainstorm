def binary_search(li: list[int], find: int) -> int:
    """
    **Function `binary_search`**:
      - Takes a sorted list of integers and an integer to find.
      - Uses the binary search algorithm to find the position of the integer in the list.
      - Returns the index of the integer if found, otherwise returns -1.
    """
    left: int = 0
    right: int = len(li) - 1

    while left <= right:
        mid: int = (left + right) // 2  # for integer division
        if li[mid] == find:
            return mid
        elif li[mid] < find:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == '__main__':
    sorted_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 15, 18, 20]
    """
    **Main block**:
      - Defines a sorted list of integers.
      - Iterates through integers from 1 to 21.
      - For each integer, it calls the `binary_search` function.
      - Prints whether the integer is found in the correct position or not in the list. If the integer is not in the 
        list, it prints that the integer is not in the list.
    """
    for x in range(1, 22):
        position = binary_search(sorted_list, x)

        if position == -1:
            if x in sorted_list:
                print(x, 'is in List, but function returned -1')
            else:
                print(x, "not in list")
        else:
            if sorted_list[position] == x:
                print(x, 'found in correct position')
            else:
                print('binary search returned', position, 'for', x, 'which is incorrect')
    print('program end')
