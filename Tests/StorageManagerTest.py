import unittest
import os
import shutil
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from StorageManager import TableManager as StorageManager 

class TestStorageManager(unittest.TestCase):
    def setUp(self):
        self.manager = StorageManager()
        if not os.path.exists("dbms"):
            os.mkdir("dbms")

    def tearDown(self):
        if os.path.exists("dbms"):
            shutil.rmtree("dbms")

    def test_create_table_success(self):
        result = self.manager.CreateTable("test_table", [1, 2, 3])
        self.assertTrue(result)
        self.assertTrue(os.path.exists("dbms/test_table.csv"))

    def test_create_table_already_exists(self):
        self.manager.CreateTable("test_table", [1, 2, 3])
        result = self.manager.CreateTable("test_table", [4, 5, 6])
        self.assertFalse(result)

    def test_create_table_invalid_name(self):
        result = self.manager.CreateTable("", [1, 2, 3])
        self.assertFalse(result)

    def test_create_table_empty_columns(self):
        result = self.manager.CreateTable("empty_columns_table", [])
        self.assertTrue(result)
        self.assertTrue(os.path.exists("dbms/empty_columns_table.csv"))

if __name__ == '__main__':
    unittest.main()