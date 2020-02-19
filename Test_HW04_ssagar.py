
import unittest

from HW04_ssagar import repo_info


class TestGetInfo(unittest.TestCase):
    def test_normal_response(self):
        expected = ['User: Savitri-Sagar',
                    'Repo: test1 Number of commits: 3',
                    'Repo: test2 Number of commits: 2',
                    'Repo: Triangle567 Number of commits: 1']
        self.assertEqual(repo_info(), expected)

    def test_bad_user_name(self):
        self.assertEqual(repo_info('xxxxxxx'), 'unable to fetch repos from user')
        self.assertEqual(repo_info(''), 'unable to fetch repos from user')


if __name__ == '__main__':
    unittest.main()