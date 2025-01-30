def count_digits(n: int) -> int:
    count = 0  # Инициализируем счётчик
    if n == 0:  # Если число равно 0, сразу возвращаем 1
        return 1
    while n > 0:  # Пока число не станет 0
        n = n // 10  # Убираем последнюю цифру числа
        count += 1  # Увеличиваем счётчик
    return count  # Возвращаем количество цифр


# Do not change the below's code
if __name__ == "__main__":
    assert count_digits(0) == 1
    assert count_digits(134) == 3
    assert count_digits(54) == 2
    assert count_digits(55678) == 5
