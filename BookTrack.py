feature/add-book
books = [] 
import json
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
def load_books():
    file=open("books.json","r",encoding="utf-8")
    dt=json.load(file)
    file.close()
    return dt
def save_books(books):
    file=open("books.json","w",encoding="utf-8")
    json.dump(books,file)
    file.close()
main
def main():
    while True:
        # Показать меню
        # Вызвать нужную функцию
        break
if __name__ == "__main__":
    main()
