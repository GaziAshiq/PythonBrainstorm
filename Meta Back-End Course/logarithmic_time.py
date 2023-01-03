def find_number_log(target):
    iterations = 0
    x = range(1000)
    # print(type(x))
    left = 0
    right = len(x) - 1

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        isNumber = x[mid]

        if target == isNumber:
            print("Iterations:- ", iterations)
            return mid
        elif target < isNumber:
            right = mid - 1
        else:
            left = mid + 1

    return -1


print(find_number_log(999))
