from TwitterAPI import TwitterAPI
import boto3
import json

## twitter credentials

consumer_key = "mIkoyZg5hgTul8VLb0AyIAfdV"
consumer_secret = "NDETD7PDY9SfgQwgSVwVD7zb1WJHijM8FUOACFzfNdyM63qSfi"
access_token_key = "155263055-COpdWg8pVMuwYMmUscIZrdLwpni5l7EN2Mzf7TNM"
access_token_secret = "7qC6fwBL2Xhy2Nj5ekZlOcKLHMVNo6dJxTXbciTAH02hk"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

kinesis = boto3.client('kinesis',
region_name='us-west-2',
aws_access_key_id='AKIAJ2CQZHOYGX5AB4DA',
aws_secret_access_key='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')

r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})

tweets = []
count = 0
for item in r:
    jsonItem = json.dumps(item)
    tweets.append({'Data':jsonItem, 'PartitionKey':"filler"})
    count += 1
    if count == 100:
        kinesis.put_records(StreamName="twitter", Records=tweets)
        count = 0
        tweets = []