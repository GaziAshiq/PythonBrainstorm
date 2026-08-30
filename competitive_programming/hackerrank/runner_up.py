if __name__ == '__main__':
    n = int(input())
    arr = sorted(set(list(map(int, input().split()))), reverse=True)[1]
    print(arr)
