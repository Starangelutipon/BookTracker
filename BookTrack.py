import json

books = [] 
def add_book():
    name=input('название: ').strip()
    author=input('автор: ').strip()
    time=input('дата прочтения (ч/м): ').strip()
    rate=int(input('оценка(от 1 до 5): '))
    if rate<1 or rate>5:
        print('оценка от 1 до 5')
        return
    for book in books:
        if book['имя'].lower()==name.lower() and book['автор'].lower()==author.lower():
            print("книга есть в списке")
            return
    books.append({
        'имя': name,
        'автор': author,
        'оценка': rate,
        'дата': time
    })
    print("книга добавлена")
def delete():
    name=input('название: ').strip()
    author=input('автор: ').strip()
    for book in books:
        if name.lower()==book['имя'].lower() and author.lower()==book['автор'].lower():
            books.remove(book)
            print('книга удалена')
            return
    print('ошибка в имени автора или названии')
def list_and_stats(x):
    m_rate=0
    if books==[]:
        print('нет прочитанных книг')
        return
    if x==0:
        for book in books:
            print(f"книга {book['имя']};автор {book['автор']};дата прочтения {book['дата']};оценка {book['оценка']}")
    elif x==1:
        for book in books:
            m_rate+=book['оценка']
        av_rate=m_rate/len(books)
        print(av_rate)
    elif x==2:
        stats = {}
        for book in books:
            author=book['автор']
            stats[author]=stats.get(author, 0)+1
            print('статистика по авторам')
        for author, count in stats.items():
            print(f'автор: {author};кол-во книг: {count}')
        
def load_books():
    file=open("books.json","r",encoding="utf-8")
    dt=json.load(file)
    file.close()
    return dt
def save_books(books):
    file=open("books.json","w",encoding="utf-8")
    json.dump(books,file)
    file.close()
def main():
    global books
    books=load_books()
    while True:
        print('1.Добавить книгу\n2.Показать все книги\n3.Показать среднюю оценку\n4.Статистика по авторам\n5.Удалить книгу\n6.Выход')
        choice=input('выбор: ')
        if choice=='1':
            add_book()
            save_books(books)
        if choice=='2':
            x=0
            list_and_stats(x)
        if choice=='3':
            x=1
            list_and_stats(x)
        if choice=='4':
            x=2
            list_and_stats(x)
        if choice=='5':
            delete()
            save_books(books)
        if choice=='6':
            break
if __name__ == "__main__":
    main()
