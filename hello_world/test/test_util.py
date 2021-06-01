import boto3
from moto import mock_dynamodb2


@mock_dynamodb2
def create_mock_table():
    """
    Create sample DynamoDB table
    Created by Daiki
    :return: mock table
    """
    mock_dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
    mock_table = mock_dynamodb.create_table(
        TableName="DPCode",
        KeySchema=[
            {
                'AttributeName': 'PK',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'SK',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'PK',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'SK',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 2,
            'WriteCapacityUnits': 2
        }
    )

    return mock_table
