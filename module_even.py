"""Модуль 2: парні числа ряду від 0 до 20."""


def even_numbers(start=0, end=20):
    return [i for i in range(start, end + 1) if i % 2 == 0]