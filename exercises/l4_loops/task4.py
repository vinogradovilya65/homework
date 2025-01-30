def find_max(l: list[int]) -> int | None:
    if not l:  # Проверяем, пуст ли список
        return None
    
    max_val = l[0]  # Начинаем с первого элемента
    for num in l:  # Перебираем все элементы списка
        if num > max_val:  # Если текущий элемент больше max_val, обновляем max_val
            max_val = num
    
    return max_val  # Возвращаем максимальное значение


# Do not change the below's code
if __name__ == "__main__":
    assert find_max([3, 1, 4, 3]) == 4
    assert find_max([3, 1, 4, 3, 8, 7]) == 8
    assert find_max([1]) == 1
    assert find_max([]) == None

