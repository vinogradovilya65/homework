def odd_str(n: int) -> str:
    s = ""

    # Use for loop to run from 0 to n (included) 
    # and form a string `s`.
    # String `s` will contain only odd numbers from interval [0; n].
    for i in range(n + 1):  # Перебираем числа от 0 до n
        if i % 2 != 0:  # Проверяем, если число нечетное
            s += str(i)  # Добавляем нечетное число в строку

    return s


# Do not change the below's code
if __name__ == "__main__":
    assert odd_str(4) == "13"
    assert odd_str(6) == "135"
    assert odd_str(8) == "1357"
