import boto3
from datetime import datetime, timezone

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_list = s3.list_buckets()
    
    for bucket in bucket_list['Buckets']:
        bucket_name = bucket['Name']
        print(f"Processing bucket: {bucket_name}")
        
        # List objects in the bucket
        response = s3.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            for obj in response['Contents']:
                last_modified = obj['LastModified']
                current_date = datetime.now(timezone.utc)
                days_since_last_modified = (current_date - last_modified).days
                
                # Transition objects older than 30 days to Glacier
                if days_since_last_modified > 30:
                    s3.copy_object(
                        Bucket=bucket_name,
                        CopySource={'Bucket': bucket_name, 'Key': obj['Key']},
                        Key=obj['Key'],
                        StorageClass='GLACIER'
                    )
                    print(f"Moved object {obj['Key']} in bucket {bucket_name} to Glacier.")
                    
                    # Optionally, delete the original object after copying
                    s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
                    print(f"Deleted object {obj['Key']} in bucket {bucket_name}.")
            
            # Check if the bucket is empty after processing all objects
            empty_response = s3.list_objects_v2(Bucket=bucket_name)
            if 'Contents' not in empty_response:
                # Delete the bucket if it is empty
                s3.delete_bucket(Bucket=bucket_name)
                print(f"Deleted bucket {bucket_name} as it was empty.")
        else:
            print(f"No objects found in bucket {bucket_name}.")
            # Optionally delete empty buckets immediately
            s3.delete_bucket(Bucket=bucket_name)
            print(f"Deleted bucket {bucket_name} as it was empty.")