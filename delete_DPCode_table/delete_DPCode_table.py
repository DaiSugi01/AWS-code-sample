import boto3
import json

table_name: str = "DPCode"
pk: str = "PK"
sk: str = "SK"


def delete_table(dynamodb=None):
    """
    Delete table
    :param dynamodb: dynamodb
    """
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)

    if table:
        table.delete()

    print("DELETE SUCCESS")


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    delete_table(dynamodb)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
