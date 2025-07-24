import pytest
import re

def is_malicious(input_str):
    return bool(re.search(r'<script>', input_str, re.IGNORECASE))

@pytest.mark.parametrize("input_str", [
    "<script>alert('xss')</script>",
    "normal text"
])
def test_reject_malicious(input_str):
    assert not is_malicious(input_str)
