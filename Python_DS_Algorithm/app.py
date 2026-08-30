def solution(num, str_li):
    x = len(str_li)
    li = []
    for i in range(x):
        li.append(num + i)
    return li

print(solution(1, ['a', 'b', 'c', 'd', 'e']))  # [1, 2, 3, 4, 5]
