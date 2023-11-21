import unittest
from datetime import datetime
from app import app, tasks

class TestIntegration(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        tasks.clear()  # Clear tasks before each test
    
    def test_add_and_view_tasks(self):
        # Simulate adding a task
        task_data = {'task': 'Test Task', 'due_date': '2023-11-30'}
        self.app.post('/add', data=task_data, follow_redirects=True)

        # Simulate viewing tasks
        response = self.app.get('/vw_tasks')

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Task', response.data)
        self.assertIn(b'2023-11-30', response.data)


    def test_delete_and_view_tasks(self):
        # Add a task for testing
        tasks.append({'task': 'Test Task', 'due_date': datetime.now()})

        # Simulate deleting the task
        response = self.app.get('/delete/0', follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(tasks), 0)

        # Simulate viewing tasks after deletion
        response = self.app.get('/view_tasks')

        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Test Task', response.data)

if __name__ == '__main__':
    unittest.main()
