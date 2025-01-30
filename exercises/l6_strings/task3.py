def take(s: str, n: int, last: bool = False) -> str:
    # If n is less than or equal to 0, return an empty string
    if n <= 0:
        return ""
    
    # If last is False, return the first n characters
    if not last:
        return s[:n]
    
    # If last is True, return the last n characters
    return s[-n:]


# Do not change the below's code
if __name__ == "__main__":
    assert take("abcde", 2) == "ab"
    assert take("bbhj", 3) == "bbh"
    assert take("bjk", 0) == ""
    assert take("bjk", -1) == ""

    assert take("abcd", 2, True) == "cd"
    assert take("agfd", 4, True) == "agfd"
    assert take("df", 10, True) == "df"
    assert take("fff", -1, True) == ""
