"""Завдання 2. Основна програма з меню вибору функцій з модулів."""
from module_expression import calc_y
from module_even import even_numbers


def main():
    while True:
        print("\nМЕНЮ")
        print("1 - Обчислити y = ln(x + 1) + sqrt(x)")
        print("2 - Парні числа від 0 до 20")
        print("0 - Вихід")
        choice = input("Ваш вибір: ").strip()
        if choice == "1":
            try:
                x = float(input("Введіть x: ").replace(",", "."))
                print(f"y = {calc_y(x):.4f}")
            except ValueError as e:
                print(f"Помилка: {e}")
        elif choice == "2":
            print("Парні числа:", *even_numbers())
        elif choice == "0":
            print("Завершення роботи.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()