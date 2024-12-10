
def find_index(list_, item):   # Задаю функцию для поиска индекса
    for i in list_:   # Задаю цикл для поиска слова в списке
        if i in item:   # Задаю условие для поиска слова в цикле
            index1 = list_.index(item)   # Нахожу индекс методом index и присваиваю его значение локальной переменной
            return index1   # Возвращаю переменную
    # Если слова в списке не найдется, функция вернет значение None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
