# tests/__init__.py

import os
import pytest

@pytest.fixture(scope="module")
def test_credits_file(tmpdir):
    """Fixture to create a temporary credits file for testing."""
    credits_file = tmpdir.join("test_credits.cfg")
    credits_file.write("Test Credits:\n- Test Developer")
    return credits_file
