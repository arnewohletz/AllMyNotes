from abc import ABC


# Subject
class BookParser(ABC):

    def get_number_of_pages(self):
        pass


# RealSubject
class RealBookParser(BookParser):

    def __init__(self, book: str):
        # some expensive computation
        print("Puuh, I'm finally done with book ...")

    def get_number_of_pages(self):
        print("That's quickly done ...")
        # returning pages


# Proxy
class LazyBookParserProxy:

    def __init__(self, book: str):
        self.book = book
        self.book_parser = None

    def get_number_of_pages(self):
        if not self.book_parser:
            self.book_parser = RealBookParser(self.book)
        return self.book_parser.get_number_of_pages()
