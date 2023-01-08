"""2зад. да се сътави програма на Python, чрез която да се дефинира
клас Вооk с полета: book_name (име на книга), book_code (код на книга), book_price (Цена на книга),
book_year (година на издаване), book_author (автор на книга).
Да се дефинира конструктор, който инициализира полетата на класа. (6 Т.)
Да се създаде списък с име books, който съдъжа четири инстанции на класа Вооk.
Да се съставят две функции: порвата функция с име sort_name да извршва сортиране
по име на книга (book_name) в низходящ ред и да извежда получения резултат на екрана.
Втората функция с име author да извежда на екрана всички книги от един автор. (16 т.)
Да се състави функция с име search_book, която получава като аргумент код на книга (book_code).
Ако торсената книга е налична да се изведе нейната година на издаване ( book_year).
Ако тырсената книга не е налична да се изведе съобщение на екрана , The book is not found!". (16 T.)
"""


class Book:
    def __init__(self, book_name, book_code, book_price, book_year, book_author):
        self.book_name = book_name
        self.book_code = book_code
        self.book_price = book_price
        self.book_year = book_year
        self.book_author = book_author

    def __repr__(self):
        return f'{self.book_code} {self.book_name} {self.book_price} \
    {self.book_author} {self.book_year}'

    def __lt__(self, other):
        return self.book_name < other.book_name


books = [
    Book('A1', 121, 12.34, 2022, 'BC'),
    Book('A1', 124, 34.22, 2021, 'BB'),
    Book('A2', 125, 20, 2022, 'BC'),
    Book('A3', 120, 7.43, 2021, 'AC')
]


def sort_books():
    print(sorted(books, reverse=True))


def sort_author(author):
    for book in books:
        if book.book_author == author:
            print(author)


def search_book(code):
    for book in books:
        if book.book_code == code:
            print(book.book_year)
        return
    print('The book is not found!')

print(books)
sort_books()
sort_author('BC')
sort_author('XY')
search_book(119)
search_book(121)
