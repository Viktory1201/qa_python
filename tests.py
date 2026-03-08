from main import BooksCollector
import pytest
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
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.fixture
    def collector(self):
        return BooksCollector()

    def test_add_new_book_valid_name_success(self, collector):
        collector.add_new_book("Ромео и Джульетта")
        assert "Ромео и Джульетта" in collector.books_genre
        assert collector.books_genre["Ромео и Джульетта"] == ''

    def test_add_new_book_name_too_long_ignored(self, collector):
        long_name = "a" * 41
        collector.add_new_book(long_name)
        assert long_name not in collector.books_genre

    def test_add_new_book_duplicate_ignored(self, collector):
        collector.add_new_book("Гамлет")
        collector.add_new_book("Гамлет")
        assert len(collector.books_genre) == 1

    def test_set_book_genre_valid_book_and_genre_success(self, collector):
        collector.add_new_book("Недоросль")
        collector.set_book_genre("Недоросль", "Комедии")
        assert collector.get_book_genre("Недоросль") == "Комедии"

    def test_set_book_genre_nonexistent_book_ignored(self, collector):
        collector.set_book_genre("Не существующая книга", "Фантастика")
        assert "Не существующая книга" not in collector.books_genre

    def test_get_book_genre_existing_book_returns_genre(self, collector):
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        assert collector.get_book_genre("Мастер и Маргарита") == "Фантастика"

    def test_get_books_with_specific_genre_valid_genre_returns_list(self, collector):
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Комедии")
        collector.set_book_genre("Книга 2", "Комедии")
        result = collector.get_books_with_specific_genre("Комедии")
        assert result == ["Книга 1", "Книга 2"]

    def test_get_books_genre_returns_current_dictionary(self, collector):
        collector.add_new_book("Книга")
        result = collector.get_books_genre()
        assert isinstance(result, dict)
        assert "Книга" in result

    def test_get_books_for_children_returns_books_without_age_rating(self, collector):
        collector.add_new_book("Мультфильм 1")
        collector.add_new_book("Ужас 1")
        collector.set_book_genre("Мультфильм 1", "Мультфильмы")
        collector.set_book_genre("Ужас 1", "Ужасы")
        result = collector.get_books_for_children()
        assert "Мультфильм 1" in result
        assert "Ужас 1" not in result

    def test_add_book_in_favorites_existing_book_success(self, collector):
        collector.add_new_book("Любимая книга")
        collector.add_book_in_favorites("Любимая книга")
        assert "Любимая книга" in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_add_book_in_collector_ignored(self, collector):
        collector.add_book_in_favorites("Книга не из коллекции")
        assert "Книга не из коллекции" not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate_ignored(self, collector):
        collector.add_new_book("Повторяющаяся книга")
        collector.add_book_in_favorites("Повторяющаяся книга")
        collector.add_book_in_favorites("Повторяющаяся книга")
        assert collector.get_list_of_favorites_books().count("Повторяющаяся книга") == 1

    def test_delete_book_from_favorites_existing_book_removed(self, collector):
        collector.add_new_book("Удаляемая книга")
        collector.add_book_in_favorites("Удаляемая книга")
        collector.delete_book_from_favorites("Удаляемая книга")
        assert "Удаляемая книга" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_returns_current_list(self, collector):
        collector.add_new_book("Фаворит 1")
        collector.add_new_book("Фаворит 2")
        collector.add_book_in_favorites("Фаворит 1")
        collector.add_book_in_favorites("Фаворит 2")
        result = collector.get_list_of_favorites_books()
        assert isinstance(result, list)
        assert "Фаворит 1" in result
        assert "Фаворит 2" in result