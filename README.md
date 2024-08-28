AWS Lambda Functions for Cost Optimization
Overview
This repository contains two AWS Lambda functions designed for cost optimization in AWS:

EBS Snapshot Deletion Lambda Function
S3 Bucket Optimization Lambda Function
Both functions are available as files in this repository.

Lambda Functions
1. EBS Snapshot Deletion Lambda Function
Description: This Lambda function identifies and deletes stale EBS snapshots to reduce AWS costs. It removes snapshots that are not attached to any volume or whose associated volumes are not attached to any running EC2 instances.

2. S3 Bucket Optimization Lambda Function
Description: This Lambda function optimizes S3 bucket storage by transitioning objects older than 30 days to the Glacier storage class and deleting empty buckets.

Setup Instructions
1. Deploying Lambda Functions
Create a New Lambda Function:

Sign in to the AWS Management Console.
Navigate to the Lambda service.
Click "Create function."
Choose "Author from scratch."
Enter a name for your function.
Select "Python 3.x" as the runtime.
Create a new role with basic Lambda permissions or choose an existing role.
Upload the Code:

In the Lambda function console, upload the respective code file from this repository.
Adjust the IAM role permissions if necessary to ensure the Lambda function can access EC2 and S3 resources.
2. Setting Up CloudWatch Triggers
Create a CloudWatch Rule:

Navigate to the CloudWatch service in the AWS Management Console.
Click "Rules" under the "Events" section.
Click "Create rule."
Choose "Event Source" as "Event Pattern" and configure the rule to match your desired schedule (e.g., daily or weekly).
Add the Lambda Function as a Target:

Under "Targets," click "Add target."
Select "Lambda function" and choose the Lambda function you deployed.
Click "Configure details" and provide a name for the rule.
Click "Create rule."
Your Lambda functions are now set up to run on a schedule defined by your CloudWatch rule. The EBS Snapshot Deletion function will clean up old snapshots, and the S3 Bucket Optimization function will transition old objects to Glacier and delete empty buckets.

Files
stale-snapshot-delete.py: Contains the code for the EBS Snapshot Deletion Lambda Function.
s3-bucket-optimize.py: Contains the code for the S3 Bucket Optimization Lambda Function.
For further details, refer to the individual files.