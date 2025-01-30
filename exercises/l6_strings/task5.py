def has_prefix(s: str, prefix: str) -> bool:
    return s.startswith(prefix)

# Do not change the below's code
if __name__ == "__main__":
    assert has_prefix("apple", "app") is True
    assert has_prefix("apple", "a") is True
    assert has_prefix("apple", "applg") is False
    assert has_prefix("", "") is True
