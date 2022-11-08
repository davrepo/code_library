"""An example of a test module for the Program module."""

from Total import total

def test_total_empty() -> None:
    """Total of empty list should be 0.0"""
    assert total([]) == 0.0
    
def test_total_single() -> None:
    """Total of a single item list should be that item"""
    assert total([1.0]) == 1.0

def test_total_multiple() -> None:
    """Total of a multiple item list should be the sum of all items"""
    assert total([1.0, 2.0, 3.0]) == 6.0