import boto3
import s3fs
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import io

def convert_flat_file_to_parquet(bucket_name, flat_file_key, parquet_file_key):
    s3 = boto3.client('s3')
    s3_file_path = f"s3://{bucket_name}/{flat_file_key}"
    s3_parquet_path = f"s3://{bucket_name}/{parquet_file_key}"

    try:
        df = pd.read_csv(s3_file_path)
        print(f"CSV file {flat_file_key} loaded into DataFrame.")
        table = pa.Table.from_pandas(df)
        buffer = io.BytesIO()
        pq.write_table(table, buffer)
        buffer.seek(0)
        
        s3.upload_fileobj(buffer, bucket_name, parquet_file_key)
        print(f"Converted and uploaded Parquet file to {parquet_file_key} in S3.")
        return True

    except Exception as e:
        print(f"Failed to convert and upload {flat_file_key}: {e}")
        return False
    

    #try:
    #    obj = s3.get_object(Bucket=bucket_name, Key=flat_file_key)

    #    df = pd.read_csv(io.BytesIO(obj['Body'].read()))
    #    print(f"CSV file {flat_file_key} loaded into DataFrame.")
    #    table = pa.Table.from_pandas(df)
    #    buffer = io.BytesIO()
    #    pq.write_table(table, buffer)
    #    buffer.seek(0)
    #    

    #    s3.put_object(Bucket=bucket_name, Key=parquet_file_key, Body=buffer.getvalue())
    #    print(f"Converted and uploaded {parquet_file_key} to S3.")
    #    return True


    #except Exception as e:
    #    print(f"Failed to convert to Parquet: {e}")
    #    return False


bucket_name = "flat-file-to-parquet-with-prefixes"
    
flat_file_key = "flat_files/generated_mock_data2.csv"
    
parquet_file_key = "parquet_files/generated_mock_data.parquet" 

convert_flat_file_to_parquet(bucket_name, flat_file_key, parquet_file_key)

