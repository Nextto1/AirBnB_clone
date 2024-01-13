#!/usr/bin/python3
"""
Test for the storage
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.engine.file_storage import FileStorage


class test_fileStorage(unittest.TestCase):
    """Test used for FileStorage Class"""
    def test_instances(self):
        """chequeamos of the instantation"""
        obj = FileStorage()
        self.assertIsInstance(obj, FileStorage)

    def test_docs(self):
        """Test docstrings"""
        self.assertIsNotNone(FileStorage.all)
        self.assertIsNotNone(FileStorage.new)
        self.assertIsNotNone(FileStorage.save)
        self.assertIsNotNone(FileStorage.reload)

    if __name__ == '__main__':
        unittest.main()

