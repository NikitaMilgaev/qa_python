import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тест на добавление книг с разной длиной названия (с параметризацией)
    @pytest.mark.parametrize('book_name, expected_length', [
        ('Короткое название', 1),
        ('Вот книга с длинным названием, очень длинным, больше чем 40 символов', 0)
    ])
    def test_add_new_book_add_book_with_different_lengths(self, book_name, expected_length):
        collector = BooksCollector()

        collector.add_new_book(book_name)

        assert len(collector.get_books_genre()) == expected_length


    # Тест на установку жанра книги (с параметризацией)
    @pytest.mark.parametrize('book, genre_book', [
        ('Книга1', 'Ужасы'),
        ('Книга2', 'Фантастика')
    ])
    def test_set_book_genre(self, book, genre_book):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre_book)

        assert collector.get_book_genre(book) == genre_book

    # Тест на получение жанра книги по имени
    def test_get_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Ужасы')

        assert collector.get_book_genre('Книга') == 'Ужасы'

    # Тест на получение книг с определённым жанром
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')
        collector.add_new_book('Книга2')
        collector.set_book_genre('Книга2', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга1', 'Книга2']

    # Тест на получение словаря всех книг с жанрами
    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Книга1')
        collector.set_book_genre('Книга1', 'Фантастика')

        assert collector.get_books_genre() == {'Книга1': 'Фантастика'}

    # Тест на получение книг, подходящих для детей
    def test_get_books_for_childrenbook(self):
        collector = BooksCollector()

        collector.add_new_book('Книга для детей')
        collector.set_book_genre('Книга для детей', 'Мультфильмы')
        collector.add_new_book('Книга для взрослых')
        collector.set_book_genre('Книга для взрослых', 'Ужасы')

        assert collector.get_books_for_children() == ['Книга для детей']

    # Тест на добавление книги в избранное
    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Избранная книга')
        collector.add_book_in_favorites('Избранная книга')

        assert 'Избранная книга' in collector.get_list_of_favorites_books()

    # Тест на удаление книги из избранного
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Избранная книга')
        collector.add_book_in_favorites('Избранная книга')
        collector.delete_book_from_favorites('Избранная книга')

        assert len(collector.get_list_of_favorites_books()) == 0

    # Тест на получение списка избранных книг
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Избранная книга')
        collector.add_book_in_favorites('Избранная книга')

        assert collector.get_list_of_favorites_books() == ['Избранная книга']

