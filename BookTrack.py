books = []
def delete():
    name=input('название: ').strip()
    author=input('автор: ').strip()
    for book in books:
        if name==book['имя'] and author==['автор']:
            books.remove(book)
            print('книга удалена')
            return
    print('ошибка в имени автора или названии')
def load_books():
    pass
def save_books(books):
    pass
def main():
    while True:
        # Показать меню
        # Вызвать нужную функцию
        break
if __name__ == "__main__":
    main()
