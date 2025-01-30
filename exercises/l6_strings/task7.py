def contains_vowels(s: str) -> bool:
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            return True
    return False


# Do not change the below's code
if __name__ == "__main__":
    assert contains_vowels("aghfn") is True
    assert contains_vowels("bnv") is False
    assert contains_vowels("AER") is True
    assert contains_vowels("LKU") is True
