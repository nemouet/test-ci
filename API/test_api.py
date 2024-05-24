import unittest
from unittest import mock
import json
import mongomock
from run import app


def mockdatabase():
    clientMongo = mongomock.MongoClient()
    db = clientMongo["student_db"]
    collection = db["students"]
    collection.insert_one(
        {
            "full_name": "Init student",
            "birth_year": "1945",
            "major": "AI",
            "unversity": "ITMO",
            "gender": "Nam",
        }
    )
    return collection


class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.test_data = {
            "fullName": "Nguyen Van CDE",
            "doB": "2001",
            "gender": "Nam",
            "school": "NEUST"
        }

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

    def test_create_student(self):
        response = self.app.post('/api/students', json=self.test_data)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
