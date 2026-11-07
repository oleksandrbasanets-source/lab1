"""Модуль 1: обчислення виразу y = ln(x + 1) + sqrt(x)."""
import math


def calc_y(x):
    if x < 0:
        raise ValueError("x має бути невід'ємним (x >= 0)")
    return math.log(x + 1) + math.sqrt(x)