import pytest
import mimetypes

def is_valid_file(filename, filesize):
    allowed_types = ['image/png', 'image/jpeg']
    max_size = 2 * 1024 * 1024
    mime = mimetypes.guess_type(filename)[0]
    return mime in allowed_types and filesize <= max_size

@pytest.mark.parametrize("filename,filesize", [
    ("test.png", 1024),
    ("malicious.exe", 1024)
])
def test_file_upload(filename, filesize):
    assert is_valid_file(filename, filesize)
