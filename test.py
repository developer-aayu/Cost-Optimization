import boto3

client = boto3.client('s3')         #use the client to specify the service used

response = client.delete_bucket(
    Bucket='aayu-test-bucket-1409',
    ExpectedBucketOwner='975050175364'
)

print(response)