# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest
class Column:
    '''
    Класс описывает модель строительной колонны.
    '''
    def __init__(self, height: Union[int, float], radius: Union[int, float]):
        '''
        Инициализация экземпляра класса.

        :param height: Высота колонны.
        :param radius: Радиус колонны.

        Example:
        >>> column = Column(5, 0.2)
        '''
        if height <= 0:
            raise ValueError('Значение должно быть положительным')
        if not isinstance(height, (int, float)):
            raise TypeError('Значение должно быть типа int или float')
        self.height = height

        if radius <= 0:
            raise ValueError('Значение должно быть положительным')
        if not isinstance(radius, (int, float)):
            raise TypeError('Значение должно быть типа int или float')
        self.radius = radius

    def increase_height(self, increase_height: (int, float)):
        '''
        Метод увеличивает высоту колонны на заданное значение
        :param increase_height: Значение, на которое увеличиваем колонну
        '''
        if increase_height <= 0:
            raise ValueError('Значение должно быть положительным')
        if not isinstance(increase_height, (int, float)):
            raise TypeError('Значение должно быть типа int или float')
        self.height += increase_height

    def increase_radius(self, increase_radius: (int, float)):
        '''
        Метод увеличивает радиус колонны на заданное значение
        :param increase_radius: Значение, на которое увеличиваем радиус
        '''
        ...

class FireProtection:
    '''
    Класс описывает модель огнезащитного материала.
    '''
    def __init__(self, time_on_fire: int, cost: int, name_of_material: str):
        '''
        Инициализация экземпляра класса.

        :param time_on_fire: Время, которое материал выдерживает под воздействием огня до потери несущей способности.
        :param cost: Цена материала за 1 кг.
        :param name_of_material: Название материала.
        '''
        if time_on_fire <= 0:
            raise ValueError('Значение должно быть положительным')
        if not isinstance(time_on_fire, int):
            raise TypeError('Значение должно быть типа int')
        self.time_on_fire = time_on_fire

        if cost < 0:
            raise ValueError('Укажите положительную цену. При значении 0 - материал бесплатный')
        if not isinstance(cost, int):
            raise TypeError('Значение должно быть типа int')
        self.cost = cost

        if not isinstance(name_of_material, str):
            raise TypeError('Значение должно быть типа str')
        self.name_of_material = name_of_material

    def price_in_bulk(self, discont_rate: int, count: int):
        '''
        Метод описывает цену матеариала при его закупке оптом.
        :param discont_rate: Коэффициент скидки.
        :param count: Количество покупаемого товара.
        '''
        ...

class Games:
    '''
    Класс описывает модель компьютерной игры.
    '''
    def __init__(self, name: str, size: int, genre: str):
        '''
        Инициализация экземпляра класса.

        :param name: Название игры.
        :param size: Место, занимаемое игрой на жестком диске.
        :param genre: Жанр игры.
        '''
        if not isinstance(name, str):
            raise TypeError('Значение должно быть типа str')
        self.name = name

        if size <= 0:
            raise ValueError('Значение должно быть положительным')
        if not isinstance(size, int):
            raise TypeError('Значение должно быть типа int')
        self.size = size

        if not isinstance(genre, str):
            raise TypeError('Значение должно быть типа str')
        self.genre = genre

    def time_in_game(self, time_per_session: int):
        '''
        Метод считывает время в игре за одну сессию для подсчета суммарного времени, проведённого в игре.
        :param time_per_session: Время, проведенное в игре за одну сесссию.
        '''
        ...

    def difficult(self, new_difficult: str, difficult_list: list[str]):
        '''
        Метод позволяет изменить сложность игры.
        :param new_difficult: Новая сложность.
        :param difficult_list: Список режимов сложности.
        '''
        ...

if __name__ == "__main__":

    #TODO работоспособность экземпляров класса проверить с помощью doctest

    doctest.testmod()
    pass
