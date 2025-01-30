# Write the function body to make the script work without errors.
#
# HINT:
# Use while loop to count sum from 0 to n (included)
def sum_to(n: int) -> int:
    total = 0  # Инициализируем переменную для хранения суммы
    i = 0  # Счетчик, начиная с 0
    while i <= n:
        total += i  # Добавляем текущее значение i к общей сумме
        i += 1  # Переходим к следующему числу
    return total  # Возвращаем итоговую сумму

# Do not change the below's code
if __name__ == "__main__":
    assert sum_to(1) == 1
    assert sum_to(2) == 3
    assert sum_to(3) == 6
    assert sum_to(4) == 10
