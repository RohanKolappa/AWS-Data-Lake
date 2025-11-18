#pass bucket name and file name as input when running python3 command

import boto3
import csv
import os



def upload_file_to_s3(file_name, bucket_name, s3_file_name=None):
    if s3_file_name is None:
        s3_file_name = f"flat_files/{os.path.basename(file_name)}"    

    print(file_name)
    print(bucket_name)
    print(s3_file_name)
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket_name, s3_file_name)
        print(f"""{file_name} uploaded to {bucket_name} as {s3_file_name}""")
        return True

    except Exception as e:
        print("Failed to upload {file_name} to S3")
        return False


file_name = "generated_mock_data2.csv"
bucket_name = "flat-file-to-parquet-with-prefixes"


upload_file_to_s3(file_name, bucket_name)         
