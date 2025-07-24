import pytest
import html

def escape_html(user_input):
    return html.escape(user_input)

@pytest.mark.parametrize("user_input", [
    "<script>alert('xss')</script>",
    "Hello, world!"
])
def test_html_escape(user_input):
    escaped = escape_html(user_input)
    assert '<' not in escaped and '>' not in escaped
