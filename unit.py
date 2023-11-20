# import unittest
# from datetime import datetime
# from app import app, tasks

# class TestApp(unittest.TestCase):
    
#     def setUp(self):
#         self.app = app.test_client()
#         self.app.testing = True
#         tasks.clear()  # Clear tasks before each test

#     def test_index(self):
#         response = self.app.get('/')
#         self.assertEqual(response.status_code, 200)
    
#     def test_add(self):
#         task_data = {'task': 'Test Task', 'due_date': '2023-11-30'}
#         response = self.app.post('/add', data=task_data, follow_redirects=True)

#         # Check if the task is present in the tasks list
#         self.assertEqual(response.status_code, 200)  # Assuming successful redirect
#         self.assertIn({'task': 'Test Task', 'due_date': datetime(2023, 11, 30)}, tasks)

#     def test_view_tasks(self):
#     # Add a sample task to the tasks list for testing
#         tasks.append({'task': 'Test Task', 'due_date': datetime(2023, 11, 30)})

#         response = self.app.get('/view_tasks')
#         self.assertEqual(response.status_code, 200)

#         # Check if the added task data is present in the rendered HTML
#         self.assertIn(b'Test Task', response.data)
#         self.assertIn(b'2023-11-30', response.data)
#     # You may need to adjust this based on your actual data and HTML structure

    
#     def test_delete_valid_id(self):
#         tasks.append({'task': 'Test Task', 'due_date': datetime.now()})
#         response = self.app.get('/delete/0')
#         self.assertEqual(response.status_code, 302)  # Redirect status


# if __name__ == '__main__':
#     unittest.main()

from datetime import datetime
import unittest
from app import app, tasks

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        tasks.clear()  # Clear tasks before each test
    
    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add(self):
        task_data = {'task': 'Test Task', 'due_date': '2023-11-30'}
        response = self.app.post('/add', data=task_data, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn({'task': 'Test Task', 'due_date': datetime(2023, 11, 30)}, tasks)

    def test_delete_valid_id(self):
        tasks.append({'task': 'Test Task', 'due_date': datetime.now()})
        response = self.app.get('/delete/0')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(tasks), 0)

    def test_delete_invalid_id(self):
        response = self.app.get('/delete/0')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(tasks), 0)

    def test_view_tasks(self):
        response = self.app.get('/view_tasks')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

