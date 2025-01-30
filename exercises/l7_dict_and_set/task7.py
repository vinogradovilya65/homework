def merge(d1: dict[Any, Any], d2: dict[Any, Any]) -> dict[Any, Any]:
    return {**d1, **d2}  # Merge dictionaries by unpacking their contents into a new dictionary

# Do not change the below's code
if __name__ == "__main__":
    assert merge({"a": 1, "b": 2}, {"c": 3, "d": 4}) == {"a": 1, "b": 2, "c": 3, "d": 4}

    d1, d2 = {"a": 1}, {"b": 1}
    assert merge(d1, d2) == {"a": 1, "b": 1}
    assert d1 == {"a": 1}
    assert d2 == {"b": 1}
