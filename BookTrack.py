import json
books = [] 

def add_book():
    name=input('название: ').strip()
    author=input('автор: ').strip()
    time=input('дата прочтения (ч/м): ').strip()
    rate=int(input('оценка(от 1 до 5): '))
    if rate<1 or rate>5::
        print('оценка от 1 до 5')
        return
    for book in books:
        if book['name'].lower() == name.lower() and book['author'].lower() == author.lower():
            print("книга есть в списке")
            return
    books.append({
        'имя': name,
        'автор': author,
        'оценка': rate,
        'дата': time
    })
    print("книга добавлена")
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
        author_c=input('напишите автора: ')
        book_cnt=0
        for book in books:
            if author_c==book['автор']:
                print(f"книга {book['имя']};дата прочтения {book['дата']};оценка {book['оценка']}")
                book_cnt+=1
        if book_cnt==0:
            print('книг этого автора нет')
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
    while True:
        # Показать меню
        # Вызвать нужную функцию
        break
if __name__ == "__main__":
    main()
