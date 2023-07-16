"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*ints: int):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    squares = [i * i for i in ints]
    return squares


def is_prime(num: int):
    """
    Using
    """
    if num >= 2:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    return False


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(num_list: list[int], filtered: str):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    result = ""
    if filtered == "even":
        result = filter(lambda x: x % 2 == 0, num_list)
    if filtered == "odd":
        result = filter(lambda x: x % 2 != 0, num_list)
    if filtered == "prime":
        result = filter(lambda x: is_prime(x), num_list)

    return [x for x in result]
