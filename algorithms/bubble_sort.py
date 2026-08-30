def bubble(unsorted_list):
    list_size = len(unsorted_list)
    swap = False
    for i in range(list_size):
        for j in range(list_size - i - 1):
            print(f'position i: {i}, j: {j}, and the list: {unsorted_list}')
            print(f'is {unsorted_list[j]} bigger then > {unsorted_list[j + 1]} ?')
            if unsorted_list[j] > unsorted_list[j + 1]:
                swap = True
                print(f'yes! then swap them.....')
                print(f'before swap: {unsorted_list}')
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
                print(f'after swap: {unsorted_list}')
            else:
                print(f'No!')

        if not swap:  # This is saves lots of time, if a list already sorted, the loop will stop!
            return 'This array already sorted'
    return unsorted_list


if __name__ == "__main__":
    import random

    li = [random.randint(0, 20) for _ in range(5)]
    li = [1, 2, 3, 4, 5]
    print('_Before sort: ', li)
    print('After sort_: ', bubble(li))
