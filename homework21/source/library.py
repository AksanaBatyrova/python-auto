"""Library"""


class Book:
    """This is a class for book objects

    Arguments:
    name: book name
    author: book author
    pages: total amount of pages
    isbn: international standard book number
    is_reserved: is book reserved

    Methods:
    """

    def __init__(self, name, author, pages, isbn):
        self.name = name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = False

    def get_pages(self):
        """This method return amount of pages"""
        return self.pages

    def get_isbn(self):
        """This method return ISBN of a book"""
        return self.isbn


class User:
    """This is a class for library users objects

    Arguments:
    name: user name
    taken_book: book taken by user
    reserved_book: book reserved by user

    Methods:
    take_book(): assigns the book to user
    reserve_book(): reserves book for user
    return_book(): unassign the book from user
    """

    def __init__(self, name):
        self.name = name
        self.taken_book = None
        self.reserved_book = None

    def reserved_by(self, name):
        """This method return the name of book owner"""
        return name

    def take_book(self, book):
        """This method used to take books from library"""
        if book.is_reserved is True:
            return f"'{book.name}' by {book.author} is taken by another user"
        self.taken_book = f"'{book.name}' {book.author}"
        return f"You've took '{book.name}' by {book.author}"

    def reserve_book(self, book):
        """This method used to reserve books from library"""
        if book.is_reserved is True:
            return (
                f"'{book.name}' by {book.author} is reserved by another user")
        self.reserved_book = f"'{book.name}' {book.author}"
        book.is_reserved = True
        return f"You've reserved '{book.name}' by {book.author}"

    def return_book(self, book):
        """This method used to reserve books from library"""
        if book.is_reserved is False:
            return "This book is free, nothing to return"
        self.taken_book = None
        book.is_reserved = False
        return f"You've returned '{book.name}' by {book.author}"


if __name__ == "__main__":
    allan_poe_raven = Book("The Raven", "Edgar Allan Poe", 6, 9788506007914)
    johann_goethe_faust = Book("Faust, a Tragedy",
                               "Johann Wolfgang von Goethe", 165, 1503262146)
    user1 = User("John")
    user2 = User("Jane")

    assert (allan_poe_raven.get_pages()) == 6
    assert (allan_poe_raven.get_isbn()) == 9788506007914

    assert (user1.reserve_book(allan_poe_raven)) == (
        "You've reserved 'The Raven' by Edgar Allan Poe")
    assert (user1.reserved_book) == "'The Raven' Edgar Allan Poe"

    assert (user2.take_book(allan_poe_raven)) == (
        "'The Raven' by Edgar Allan Poe is taken by another user")

    assert (user1.take_book(johann_goethe_faust)) == (
        "You've took 'Faust, a Tragedy' by Johann Wolfgang von Goethe")

    assert (user1.taken_book) == (
        "'Faust, a Tragedy' Johann Wolfgang von Goethe")

    assert (user2.reserve_book(allan_poe_raven)) == (
        "'The Raven' by Edgar Allan Poe is reserved by another user")

    assert (user1.return_book(allan_poe_raven)) == (
        "You've returned 'The Raven' by Edgar Allan Poe")

    assert (user2.return_book(allan_poe_raven)) == (
        "This book is free, nothing to return")
