import unittest
from unittest import mock

from run import app


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_list_students(self):
        with mock.patch('run.students_collection.find') as mock_find:
            mock_find.return_value = [
                {
                    '_id': '1',
                    'Name': 'John Doe',
                    'YearOfBirth': 1990,
                    'Sex': 'Male',
                    'School': 'ABC School',
                    'Major': 'Computer Science'
                },
                {
                    '_id': '2',
                    'Name': 'Jane Smith',
                    'YearOfBirth': 1995,
                    'Sex': 'Female',
                    'School': 'XYZ School',
                    'Major': 'Data Science'
                }
            ]

            response = self.app.get('/api/students')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(response.json), 2)
            self.assertEqual(response.json[0]['Name'], 'John Doe')
            self.assertEqual(response.json[1]['Major'], 'Data Science')


if __name__ == '__main__':
    unittest.main()
