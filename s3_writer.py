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
        self.batch_size = 1000
        self.data_batch = []

    def add_row(self, data):
        """Add a row to the batch. Write to S3 when the batch size is reached."""
        self.data_batch.append(data)
        if len(self.data_batch) >= self.batch_size:
            self.write_to_s3()  # Write to S3 when batch size is met
            self.data_batch = []  # Reset batch after writing to S3


    def write_to_s3(self):
        try:
            # Convert data to Pandas DataFrame
            df = pd.DataFrame(self.data_batch)

            # Convert Pandas DataFrame to Parquet format
            table = pa.Table.from_pandas(df)
            buffer = io.BytesIO()
            pq.write_table(table, buffer)

            # Upload Parquet file to S3
            file_key = f"{self.file_prefix}batch_data.parquet"
            self.s3.put_object(Bucket=self.bucket_name, Key=file_key, Body=buffer.getvalue())
            print(f"Data written to S3 as Parquet file: {file_key}")
        except Exception as e:
            print(f"Failed to write to S3: {e}")


    def flush(self):
            """Force writing the remaining data to S3 if it's below batch size."""
            if self.data_batch:
                self.write_to_s3()
                self.data_batch = []
