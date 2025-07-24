import pytest
import os
import tempfile
import sys

@pytest.mark.usefixtures("limit_privileges")
def test_temp_file_cleanup():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(b'secret')
    tmp.close()
    os.remove(tmp.name)
    assert not os.path.exists(tmp.name)

@pytest.fixture(scope="function")
def limit_privileges():
    # Simulate privilege drop
    if hasattr(os, 'setuid'):
        os.setuid(65534)
