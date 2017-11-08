import boto3
import time
import json
## aws creds are stored in ~/.boto
kinesis = boto3.client("kinesis",
aws_access_key_id='AKIAJ2CQZHOYGX5AB4DA',
aws_secret_access_key='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')
shard_id = "shardId-000000000000" #only one shard!
pre_shard_it = kinesis.get_shard_iterator(StreamName="twitter", ShardId=shard_id, ShardIteratorType="LATEST")
shard_it = pre_shard_it["ShardIterator"]
while 1==1:
    out = kinesis.get_records(ShardIterator=shard_it, Limit=1)
    shard_it = out["NextShardIterator"]
    print(out)
    time.sleep(1.0)
