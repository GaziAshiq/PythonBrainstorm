def sort(given_list: list) -> list:
    n = len(given_list)  # List size
    for i in range(n):  # for each item in the list
        min_index = i  # set the first item as the minimum
        for j in range(i + 1, n):  # for each item after the first
            next_index = j  # set the next item as the next item
            if given_list[min_index] > given_list[next_index]:
                min_index = next_index  # if the next item is less than the current minimum, set the next item as the
                # minimum
        if min_index != i:
            given_list[i], given_list[min_index] = given_list[min_index], given_list[
                i]  # if the minimum is not the first item, swap the first item with the minimum item
    return given_list


if __name__ == '__main__':
    import random
    sort_this = [random.randint(0, 99) for _ in range(10)]  # make a random list
    print('Before sort: ', sort_this)
    sort(sort_this)
    print('_After sort: ', sort_this)
