import boto3
dynamodb = boto3.resource('dynamodb',
                          region_name='us-west-2',
                          aws_access_key_id='AKIAJ2CQZHOYGX5AB4DA',
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