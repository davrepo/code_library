from Join import join

def test_join_empty() -> None:
    """Joining an empty list should return an empty string."""
    assert join([], ", ") == ""

def test_join_single() -> None:
    """Joining a single item list should return that item."""
    assert join(["a"], ", ") == "a"

def test_join_multiple() -> None:
    """Joining a multiple item list should return a string with all items joined by sep."""
    assert join(["a", "b", "c"], ", ") == "a, b, c"

def test_join_multiple_no_sep() -> None:
    """Joining a multiple item list with an empty separator should return a string with all items joined."""
    assert join(["a", "b", "c"], "") == "abc"