def min_value(d: dict[str, int]) -> int:
    return min(d.values())  # Return the minimum value from the dictionary

# Do not change the below's code
if __name__ == "__main__":
    assert min_value({"a": 3, "b": 5}) == 3
    assert min_value({"a": 10}) == 10
    assert min_value({"a": -1, "b": -1, "default": 1}) == -1
