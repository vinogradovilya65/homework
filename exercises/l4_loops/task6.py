def count_char(s: str, c: str) -> int:
    count = 0  # Инициализируем счётчик
    for char in s:  # Проходим по каждому символу строки
        if char == c:  # Если символ совпадает с искомым
            count += 1  # Увеличиваем счётчик
    return count  # Возвращаем количество вхождений


# Do not change the below's code
if __name__ == "__main__":
    assert count_char("ababa", "a") == 3
    assert count_char("ababa", "b") == 2
    assert count_char("ababa", "c") == 0
    assert count_char("cccca", "a") == 1
