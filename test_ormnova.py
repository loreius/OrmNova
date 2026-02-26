# test_ormnova.py
"""
Tests for OrmNova module.
"""

import unittest
from ormnova import OrmNova

class TestOrmNova(unittest.TestCase):
    """Test cases for OrmNova class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OrmNova()
        self.assertIsInstance(instance, OrmNova)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OrmNova()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
