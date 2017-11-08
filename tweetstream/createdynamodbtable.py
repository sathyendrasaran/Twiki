import boto3
dynamodb = boto3.resource('dynamodb',
                          aws_access_key_id='AKIAIZJNGO7OV3FMMP7Q',
                          aws_secret_access_key='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')
table = dynamodb.create_table(
    TableName='hashtags',
    KeySchema=[
        {
            'AttributeName': 'hashtag',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'hashtag',
            'AttributeType': 'S'
        }
    ],
    # pricing determined by ProvisionedThroughput
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
table.meta.client.get_waiter('table_exists').wait(TableName='hashtags')