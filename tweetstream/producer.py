from TwitterAPI import TwitterAPI
import boto3
import json

## twitter credentials

consumer_key = "XXXXXXXX"
consumer_secret = "XXXXXXXX"
access_token_key = "XXXXXXXX-XXXXXXXX"
access_token_secret = "XXXXXXXX"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

kinesis = boto3.client('kinesis',
region_name='us-west-2',
aws_access_key_id='XXXXXXXX',
aws_secret_access_key='XXXXXXXXXXXXXXXX')

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
