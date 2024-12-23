class Book:
    all_books = []

    def __init__(self, title):
        self.set_title(title)
        Book.all_books.append(self)

    def get_title(self):
        return self._title

    def set_title(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self._title = title

    title = property(get_title, set_title)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        # Retrieve authors through the Contract class
        return [contract.author for contract in Contract.all_contracts if contract.book == self]


class Author:
    all_authors = []

    def __init__(self, name):
        self.set_name(name)
        Author.all_authors.append(self)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self._name = name

    name = property(get_name, set_name)

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.set_author(author)
        self.set_book(book)
        self.set_date(date)
        self.set_royalties(royalties)
        Contract.all_contracts.append(self)

    def get_author(self):
        return self._author

    def set_author(self, author):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        self._author = author

    author = property(get_author, set_author)

    def get_book(self):
        return self._book

    def set_book(self, book):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        self._book = book

    book = property(get_book, set_book)

    def get_date(self):
        return self._date

    def set_date(self, date):
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        self._date = date

    date = property(get_date, set_date)

    def get_royalties(self):
        return self._royalties

    def set_royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")
        self._royalties = royalties

    royalties = property(get_royalties, set_royalties)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
