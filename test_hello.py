def hello():
    """Returns a hello world greeting."""
    return "Hello, World!"


def test_hello():
    """Test function for hello()."""
    result = hello()
    assert result == "Hello, World!"
    assert isinstance(result, str)
    print("Test passed: hello() returns correct greeting")


if __name__ == "__main__":
    test_hello()
    print("All tests passed!")
