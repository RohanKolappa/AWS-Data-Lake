import boto3
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import io


class S3Writer:
    def __init__(self):
        # Initialize S3 client
        self.s3 = boto3.client('s3')
        self.bucket_name = 'sqs-messages-output'
        self.file_prefix = ''

    def write(self, data):
        try:
            # Convert data to Pandas DataFrame
            df = pd.DataFrame([data])

            # Convert Pandas DataFrame to Parquet format
            table = pa.Table.from_pandas(df)
            buffer = io.BytesIO()
            pq.write_table(table, buffer)

            # Upload Parquet file to S3
            file_key = f"{self.file_prefix}data-{data.get('Email', 'default')}.parquet"
            self.s3.put_object(Bucket=self.bucket_name, Key=file_key, Body=buffer.getvalue())
            print(f"Data written to S3 as Parquet file: {file_key}")
        except Exception as e:
            print(f"Failed to write to S3: {e}")

