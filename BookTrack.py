books=[]
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
