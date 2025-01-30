def count_chars(s: str) -> dict[str, int]:
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Do not change the below's code
if __name__ == "__main__":
    assert count_chars("aabc") == {"a": 2, "b": 1, "c": 1}
    assert count_chars("abc") == {"a": 1, "b": 1, "c": 1}
    assert count_chars("") == {}
