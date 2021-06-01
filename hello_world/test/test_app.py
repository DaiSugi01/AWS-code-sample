import unittest

import app
import json


class MainTest(unittest.TestCase):
    def test_create_user_obj1(self):
        """
        test case 1 - input object without optional values
        """
        test_cases_json = open('get_all_users_test.json', 'r')
        test_cases = json.load(test_cases_json)

        res1 = app.create_user_obj(test_cases['test_case_1']['input'])
        self.assertDictEqual(res1, test_cases['test_case_1']['output'])

    def test_create_user_obj2(self):
        """
        test case 2 - input object with optional values
        """
        test_cases_json = open('get_all_users_test.json', 'r')
        test_cases = json.load(test_cases_json)

        res2 = app.create_user_obj(test_cases['test_case_2']['input'])
        self.assertDictEqual(res2, test_cases['test_case_2']['output'])
