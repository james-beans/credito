# tests/conftest.py

import pytest
import tempfile
import os

@pytest.fixture
def temp_credits_file():
    """Fixture to create a temporary credits file for tests."""
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode="w")
    temp_file.write("Credits:\n- Developer: Test User")
    temp_file.close()
    
    yield temp_file.name  # Return the file path to the test function

    # Cleanup after the test
    os.remove(temp_file.name)
