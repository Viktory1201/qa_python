# qa_python
test_add_new_book_valid_name_success() - Проверяет добавление книги с корректным названием (до 40 символов).
test_add_new_book_name_too_long_ignored() - Проверяет игнорирование книги с названием длиннее 40 символов.
test_add_new_book_duplicate_ignored() - Проверяет, что дублирующая книга не добавляется.
test_set_book_genre_valid_book_and_genre_success()- Проверяет установку жанра для существующей книги с допустимым жанром.
test_set_book_genre_nonexistent_book_ignored()- Проверяет игнорирование установки жанра для несуществующей книги.
test_get_book_genre_existing_book_returns_genre()- Проверяет получение жанра существующей книги.
test_get_books_with_specific_genre_valid_genre_returns_list() - Проверяет получение списка книг заданного жанра.
test_get_books_genre_returns_current_dictionary() - Проверяет возврат текущего словаря books_genre.
test_get_books_for_children_returns_books_without_age_rating() - Проверяет возврат книг, подходящих детям.
test_add_book_in_favorites_existing_book_success() - Проверяет добавление существующей книги в избранное.
test_add_book_in_favorites_duplicate_ignored() - Проверяет игнорирование повторного добавления книги в избранное.
test_add_book_in_favorites_not_add_book_in_collector_ignored() - Проверяет игнорирование добавления книги, не добавленной в коллекцию, в избранное.
test_delete_book_from_favorites_existing_book_removed() - Проверяет удаление книги из избранного.
test_get_list_of_favorites_books_returns_current_list() - Проверяет возврат текущего списка избранных книг.