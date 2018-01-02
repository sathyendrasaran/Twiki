import boto3

client = boto3.client('kinesis',
                      region_name='us-west-2',
                      aws_access_key_id='XXXXXXXX',
                      aws_secret_access_key='XXXXXXXX')
response = client.create_stream(
    StreamName='twitter',
    ShardCount=1
)
