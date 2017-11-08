import boto3
import time
import json
import decimal

## aws creds are stored in ~/.boto

## Connent to the kinesis stream
kinesis = boto3.client("kinesis",
                       region_name='us-west-2',
                       aws_access_key_id='AKIAJ2CQZHOYGX5AB4DA',
                       aws_secret_access_key='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')
shard_id = 'shardId-000000000000' #only one shard
shard_it = kinesis.get_shard_iterator(StreamName="twitter", ShardId=shard_id, ShardIteratorType="LATEST")["ShardIterator"]

dynamodb = boto3.resource('dynamodb',
                          region_name='us-west-2',
                          aws_access_key_id='AKIAJ2CQZHOYGX5AB4DA',
                          aws_secret_access_key='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')
table = dynamodb.Table('hashtags')

while 1==1:
    out = kinesis.get_records(ShardIterator=shard_it, Limit=100)
    for record in out['Records']:
        if 'entities' in json.loads(record['Data']):
            htags = json.loads(record['Data'])['entities']['hashtags']
            if htags:
                for ht in htags:
                    htag = ht['text']
                    # print(ht)
                    checkItemExists = table.get_item(
                        Key={
                            'hashtag':htag
                        }
                    )
                    if 'Item' in checkItemExists:
                        response = table.update_item(
                            Key={
                                'hashtag': htag
                            },
                            UpdateExpression="set htCount  = htCount + :val",
                            ConditionExpression="attribute_exists(hashtag)",
                            ExpressionAttributeValues={
                                ':val': decimal.Decimal(1)
                            },
                            ReturnValues="UPDATED_NEW"
                        )
                    else:
                        response = table.update_item(
                            Key={
                                'hashtag': htag
                            },
                            UpdateExpression="set htCount = :val",
                            ExpressionAttributeValues={
                                ':val': decimal.Decimal(1)
                            },
                            ReturnValues="UPDATED_NEW"
                        )
    shard_it = out["NextShardIterator"]
    time.sleep(1.0)