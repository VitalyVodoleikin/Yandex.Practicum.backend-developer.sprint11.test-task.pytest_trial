# test_example.py
def one_more(x):
    return x + 1

# # Вот теперь ясно: автор функции забыл про сортировку.
# def get_sort_list(string):
#     new_list = string.split(',')
#     return new_list


# Исправим функцию get_sort_list(): отсортируем список.
def get_sort_list(string):
    # Сортировка и пробел после запятой в аргументе.
    new_list = sorted(string.split(', '))  
    return new_list







def test_correct():
    assert one_more(4) == 5


def test_fail():
    assert one_more(3) == 5

# Опечатка автора теста в именах Миша/Маша
# def test_sort():
#     """Тестируем функцию get_sort_list()."""
#     result = get_sort_list('Яша, Саша, Маша, Даша')
#     assert result == ['Даша', 'Миша', 'Саша', 'Яша']


def test_sort():
    """Тестируем функцию get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result  == ['Даша', 'Маша', 'Саша', 'Яша']  # 'Маша', а не 'Миша'.
