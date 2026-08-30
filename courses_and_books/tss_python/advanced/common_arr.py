def multi_unique_number(li):
    num_list = list(li)
    unique_set = set(num_list)
    unique_list = list(unique_set)
    print(f'numbers array: {li}')
    print(f'unique numbers: {unique_set}')

    count = 0
    temp = []
    same_num_arr = []

    for i in unique_list:
        for j in num_list:
            if i == j:
                temp.append(i)
        if len(temp) > 1:
            count += 1
            same_num_arr.append(temp)

        temp = []

    if count > 1:
        for i in range(len(same_num_arr)):
            if len(same_num_arr[i]) == len(same_num_arr[i + 1]):
                return True
    else:
        return False


number = multi_unique_number([1, 2, 2, 3, 4, 4, 4, 5, 5])
# print('same numbers: ' + str(number) if number else 'no same multiple numbers')
print(number)
