import json
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
сохранение и загрузка файлов
