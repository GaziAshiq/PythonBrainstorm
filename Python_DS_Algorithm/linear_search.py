def search_book(book_list: list[str], book: str) -> int:
    for i in range(len(book_list)):
        if book_list[i] == book:
            return i
    return -1


if __name__ == '__main__':
    li: list[str] = ['Algorithm', 'Data Structure', 'Python', 'Java', 'C++', 'C#', 'JavaScript', 'HTML', 'CSS', 'React',
                     'Vue']
    print(search_book(li, 'Python'))
    print(search_book(li, 'ai'))
