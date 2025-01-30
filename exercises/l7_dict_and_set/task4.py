def max_value(d: dict[str, int]) -> int:
    return max(d.values())  # Return the maximum value from the dictionary

# Do not change the below's code
if __name__ == "__main__":
    assert max_value({"a": 3, "b": 5}) == 5
    assert max_value({"a": 10}) == 10
    assert max_value({"a": -1, "b": -1, "default": 1}) == 1
