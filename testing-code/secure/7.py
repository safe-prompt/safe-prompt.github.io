import pytest
from defusedxml.ElementTree import fromstring, ParseError

def test_disable_external_entity():
    xml = """
    <!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
    <foo>&xxe;</foo>
    """
    with pytest.raises(ParseError):
        fromstring(xml)
