class Book:
    """ базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"книга {self.name}. автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ класс для бумажной книги. """

    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("количество страниц должно быть положительным числом")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()} страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """ класс для аудиокниги. """

    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError("продолжительность должна быть числом с плавающей точкой")
        if value <= 0:
            raise ValueError("продолжительность должна быть положительным числом")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()} длительность: {self.duration} часов"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"


if __name__ == "__main__":
    try:
        book1 = Book("1984", "Джордж Оруэлл")
        print(book1)
        print(repr(book1))

        paper_book1 = PaperBook("Гордость и предубеждение", "Джейн Остин", 400)
        print(paper_book1)
        print(repr(paper_book1))

        audio_book1 = AudioBook("Убить пересмешника", "Харпер Ли", 10.2)
        print(audio_book1)
        print(repr(audio_book1))


    except Exception as e:
        print(f"произошла ошибка: {e}")
