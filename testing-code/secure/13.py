import pytest

def strict_type_check(val: int):
    assert isinstance(val, int)

@pytest.mark.parametrize("val", [1, "string", 2.5])
def test_type_check(val):
    if not isinstance(val, int):
        with pytest.raises(AssertionError):
            strict_type_check(val)
    else:
        strict_type_check(val)
