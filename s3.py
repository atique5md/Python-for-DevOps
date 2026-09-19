import logging
import boto3
from botocore.exceptions import ClientError

s3 = boto3.resource('s3')
# create  s3 Bucket 

def create_bucket(bucket_name, region):
    # Create bucket
    try:
        bucket_config = {}
        s3_client = boto3.client('s3', region_name=region)
        if region != 'ap-east-1':
            bucket_config['CreateBucketConfiguration'] = {'LocationConstraint': region}

        s3_client.create_bucket(Bucket=bucket_name, **bucket_config)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# print ("Bucket created successfully !")

bucket_name = "for-python-prep"
region = "ap-south-1"

# create_bucket(bucket_name, region)

# List s3 Bucket

def show_bucket(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)


def uplode_backup(s3, file_name, bucket_name, key_name):
    data = open(file_name, 'rb')
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("uplode successfull !!")

file_name = r"D:\phyton\Devops\backup_fill.tar.gz"



# uplode_backup(s3, file_name, bucket_name, "backup_fill.tar.gz")