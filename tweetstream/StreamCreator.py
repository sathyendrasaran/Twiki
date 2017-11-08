import boto3

client = boto3.client('kinesis',
                      region_name='us-west-2',
                      aws_access_key_id='AKIAJ2CQZHOYGX5AB4DA',
                      aws_secret_access_key='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')
response = client.create_stream(
    StreamName='twitter',
    ShardCount=1
)