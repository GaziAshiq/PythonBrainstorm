def search_book(book_list, book):
    for i in range(len(book_list)):
        if book_list[i] == book:
            return i
    return -1


if __name__ == '__main__':
    li = [10, 15, 58, 41, 25, 36, 41]
    print(search_book(li, 36))
