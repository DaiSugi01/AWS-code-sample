import boto3
import json

table_name: str = "DPCode"
pk: str = "PK"
sk: str = "SK"


def create_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName=table_name,
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
    return table


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    create_table(dynamodb)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
