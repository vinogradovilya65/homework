def count_positive(n: list[int]) -> int:
    count = 0  # Инициализируем счётчик положительных чисел
    for num in n:  # Проходим по всем элементам списка
        if num > 0:  # Если число положительное
            count += 1  # Увеличиваем счётчик
    return count  # Возвращаем количество положительных чисел


# Do not change the below's code
if __name__ == "__main__":
    assert count_positive([1, 2, -3, -4]) == 2
    assert count_positive([-1, -2, -3]) == 0
    assert count_positive([4, 5, 4, 3]) == 4
