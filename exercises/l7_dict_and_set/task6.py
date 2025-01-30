def exists(d: dict[Any, Any], key: Any) -> bool:
    return key in d  # Return True if the key exists in the dictionary, otherwise False

# Do not change the below's code
if __name__ == "__main__":
    assert exists({"a": 1, "b": 2}, "b") is True
    assert exists({"a": 1, "b": 2}, "c") is False
