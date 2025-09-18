from lib import count_common_elements


def test_count_common_elements():
    # Тест 1: Обычный случай
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [5, 6, 7, 8, 9]
    result = count_common_elements(list1, list2, list3)
    assert result == 1, f"Ожидалось 1, получено {result}"
    print("Тест 1 пройден ✓")

    # Тест 2: Все элементы одинаковые
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 2, 3]
    result = count_common_elements(list1, list2, list3)
    assert result == 3, f"Ожидалось 3, получено {result}"
    print("Тест 2 пройден ✓")

    # Тест 3: Нет общих элементов
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list3 = [7, 8, 9]
    result = count_common_elements(list1, list2, list3)
    assert result == 0, f"Ожидалось 0, получено {result}"
    print("Тест 3 пройден ✓")

    # Тест 4: Один список
    list1 = [1, 2, 3, 4, 5]
    result = count_common_elements(list1)
    assert result == 5, f"Ожидалось 5, получено {result}"
    print("Тест 4 пройден ✓")

    # Тест 5: Пустые списки
    list1 = []
    list2 = [1, 2, 3]
    result = count_common_elements(list1, list2)
    assert result == 0, f"Ожидалось 0, получено {result}"
    print("Тест 5 пройден ✓")

    # Тест 6: Дубликаты в списках
    list1 = [1, 1, 2, 2, 3]
    list2 = [1, 2, 2, 3, 3]
    list3 = [1, 1, 2, 3, 3]
    result = count_common_elements(list1, list2, list3)
    assert result == 3, f"Ожидалось 3, получено {result}"
    print("Тест 6 пройден ✓")

    print("Все тесты пройдены успешно! ✅")


if __name__ == "__main__":
    test_count_common_elements()