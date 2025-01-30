def has_char(s: str, c: str) -> bool:
    for char in s:  # Проходим по всем символам строки
        if char == c:  # Если нашли символ, возвращаем True
            return True
    return False  # Если цикл завершился и не нашли символ, возвращаем False


# Do not change the below's code
if __name__ == "__main__":
    assert has_char("lfhyt", "f") == True
    assert has_char("abbaabba", "c") == False
