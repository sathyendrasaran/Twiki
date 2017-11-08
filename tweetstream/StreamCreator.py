import boto3

client = boto3.client('kinesis',
                      aws_access_key_id='AKIAIZJNGO7OV3FMMP7Q',
                      aws_secret_access_key='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')
response = client.create_stream(
    StreamName='twitter',
    ShardCount=1
)