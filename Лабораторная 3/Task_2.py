
def find_common_participants(first_group, second_group, arg=","):
    # При указании в аргументе arg знак разеделения |, программа выдаст необходимый результат
    both_groups = list(set(first_group.split(arg)).intersection(second_group.split(arg)))
    # Разделяем на отдельные имена, переводим первый список в множество
    # Сравниваем со вторым и переводим получившееся множество в список
    both_groups.sort()  # Сотируем список по алфавитному порядку
    return both_groups  # Возвращаем готовый список


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
# При указании в аргументе arg знак разеделения |, программа выдаст необходимый результат
print(find_common_participants(participants_first_group, participants_second_group))
