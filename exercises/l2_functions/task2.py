# Declare a function named `join`
# that accepts two strings as parameters
# and returns their concatenation separated
# by whitespace ' '.

def join(s1: str, s2: str) -> str:
    return s1 + " " + s2  # Конкатенируем строки с пробелом между ними

# Do not change the below's code
if __name__ == "__main__":
    a, b = "Jon", "Doe"

    assert join(a, b) == "Jon Doe"
    assert join(b, a) == "Doe Jon"
    assert join("aba", "baba") == "aba baba"
