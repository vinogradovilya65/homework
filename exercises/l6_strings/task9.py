def proxy_join(l: list[Any]) -> str:
    # Convert all elements to strings and join them with ", "
    return ", ".join(map(str, l))


# Do not change the below's code
if __name__ == "__main__":
    assert proxy_join([1, 4, 3]) == "1, 4, 3"
    assert proxy_join(["Jon", "Arya", "Rob"]) == "Jon, Arya, Rob"
    assert proxy_join([]) == ""
