import boto3
import time
import json
## aws creds are stored in ~/.boto
kinesis = boto3.client("kinesis",
aws_access_key_id='AKIAIZJNGO7OV3FMMP7Q',
aws_secret_access_key='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')
shard_id = "shardId-000000000000" #only one shard!
pre_shard_it = kinesis.get_shard_iterator(StreamName="twitter", ShardId=shard_id, ShardIteratorType="LATEST")
shard_it = pre_shard_it["ShardIterator"]
while 1==1:
    out = kinesis.get_records(ShardIterator=shard_it, Limit=1)
    shard_it = out["NextShardIterator"]
    print out;
    time.sleep(1.0)
