import unittest
from unittest.mock import patch
from database import Database


class UnitTestDatabase(unittest.TestCase):
    def setUp(self):
        self.database = Database()

    @patch('os.environ', {'MY_SQL_PASSWORD': "Sinnlos1990!"})
    def test_create_connection(self):
        self.database.create_connection('hausarbeit')
        self.assertEqual(self.database.database_name, 'hausarbeit')
        self.assertIsNotNone(self.database.engine)
        self.assertIsNotNone(self.database.meta_data)


if __name__ == '__main__':
    unittest.main()
