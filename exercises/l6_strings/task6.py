def clean(s: str) -> str:
    return ''.join(s.split())

# Do not change the below's code
if __name__ == "__main__":
    assert clean("    c     ") == "c"
    assert clean("  d  d c ") == "ddc"
    assert clean("   ") == ""
