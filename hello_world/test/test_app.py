from moto import mock_dynamodb2
import json

import app
from test_util import create_mock_table


@mock_dynamodb2
class TestLambda(object):
    def setup_method(self, method):
        print('setup. work before running the test')
        self.test_cases_json = open('get_all_users_test.json', 'r')
        self.test_cases = json.load(self.test_cases_json)
        self.mock_table = create_mock_table()
        [self.mock_table.put_item(Item=data)
         for data in self.test_cases['mock_data']]

    def teardown_method(self, method) -> None:
        print('clean up. work after running the test')
        self.test_cases_json.close()
        del self.test_cases
        del self.mock_table

    def test_create_user_obj_with_blank(self):
        """
        test case 1
            - input object which values are blank
        """
        res1 = app.create_user_obj(self.test_cases['test_case_1']['input'])
        assert res1 == self.test_cases['test_case_1']['output']

    def test_create_user_obj_with_optional(self):
        """
        test case 2
            - input object which has optional values
        """
        res = app.create_user_obj(self.test_cases['test_case_2']['input'])
        assert res == self.test_cases['test_case_2']['output']

    def test_create_user_obj_without_any_values(self):
        """
        test case 3
            - input object which does not have any keys
        """
        res = app.create_user_obj(self.test_cases['test_case_3']['input'])
        assert res == self.test_cases['test_case_3']['output']

    def test_lambda_handler_only_students(self):
        """
        test case 4
            - check lambda whether response array is sorted
                based on created_date or not
            - should include only student data.
        """
        res = app.lambda_handler(self.test_cases['mockEvent'],
                                 self.test_cases['mockContext'])

        assert res['statusCode'] == self.test_cases['mockResult']['statusCode']
        assert res['body'] == self.test_cases['mockResult']['body']
