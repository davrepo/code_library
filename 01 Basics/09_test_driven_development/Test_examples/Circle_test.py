from Circle import circle_area
import pytest

def test_circle_area() -> None:
    """Test areas when radius >= 0."""
    assert circle_area(1) == pytest.approx(3.14159, rel=1e-5)	 # approx because of floating point errors
    assert circle_area(0) == 0
    assert circle_area(2.1) == pytest.approx(13.85436, rel=1e-5)

def test_circle_area_values() -> None:
    """Make sure value errors are raised when necessary."""
    with pytest.raises(ValueError):
        circle_area(-2)

def test_circle_area_types() -> None:
    """Make sure type errors are raised when necessary."""
    with pytest.raises(TypeError):
        circle_area(3+5j)
    with pytest.raises(TypeError):
        circle_area(True)
    with pytest.raises(TypeError):
        circle_area("radius")