"""Library keywords"""

from robot.api.deco import keyword
from homework12.task1_library import User, Book


@keyword
def create_book(name, author, pages, isbn):
    return Book(name, author, pages, isbn)


@keyword
def get_pages(book):
    return book.pages


@keyword
def get_isbn(book):
    return book.isbn


@keyword
def create_user(name):
    return User(name)


@keyword
def is_book_reserved(book):
    return book.is_reserved


@keyword
def reserve_book(user, book):
    return user.reserve_book(book)


@keyword
def return_book(user, book):
    return user.return_book(book)
