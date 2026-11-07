"""Завдання 1. Функції користувача."""


def read_number(name):
    """Зчитує число від 1 до 100 з перевіркою коректності введення."""
    while True:
        raw = input(f"Введіть {name} (число від 1 до 100): ").replace(",", ".")
        try:
            value = float(raw)
        except ValueError:
            print("Помилка: потрібно ввести число.")
            continue
        if not 1 <= value <= 100:
            print("Помилка: число має бути в межах від 1 до 100.")
            continue
        return value


def calc_x(a, b):
    """Обчислює X залежно від співвідношення a та b."""
    if a < b:
        return a / b + 1
    if a == b:
        return -1
    return (a * b - 5) / a


def pyramid(n):
    """Друкує піраміду з цифри n (n від 1 до 10)."""
    for k in list(range(n, 0, -1)) + list(range(1, n + 1)):
        print(" ".join([str(n)] * k))


def read_n():
    """Зчитує ціле N від 1 до 10 з перевіркою."""
    while True:
        raw = input("Введіть N (ціле число від 1 до 10): ")
        try:
            n = int(raw)
        except ValueError:
            print("Помилка: потрібно ввести ціле число.")
            continue
        if not 1 <= n <= 10:
            print("Помилка: N має бути від 1 до 10.")
            continue
        return n


if __name__ == "__main__":
    print("Функція 1: обчислення X")
    a = read_number("a")
    b = read_number("b")
    print(f"X = {calc_x(a, b):.4f}")
    print("Функція 2: піраміда")
    pyramid(read_n())