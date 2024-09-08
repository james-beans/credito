# tests/test_credito.py

import os
import time
import pytest
from credito import Credito

def test_credito_loading():
    credito = Credito()
    credito.config()  # Use default credits.cfg
    assert credito.credits, "Credits should not be empty after loading the default credits.cfg"

def test_credito_custom_config(test_credits_file):
    credito = Credito()
    credito.config(test_credits_file)  # Use custom temporary credits.cfg
    assert "Test Developer" in credito.credits, "Credits should load the test content"
 