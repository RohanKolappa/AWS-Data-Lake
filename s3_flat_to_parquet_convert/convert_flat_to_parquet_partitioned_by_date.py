import boto3
import s3fs
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import io

def convert_flat_file_to_parquet_partitioned_by_date(bucket_name, flat_file_key, date_column):
    s3 = boto3.client('s3')
    s3_file_path = f"s3://{bucket_name}/{flat_file_key}"

    try:
        # Step 1: Load the CSV file from S3 into a Pandas DataFrame
        df = pd.read_csv(s3_file_path)
        print(f"CSV file {flat_file_key} loaded into DataFrame.")

        # Step 2: Ensure the date_column is in datetime format
        df[date_column] = pd.to_datetime(df[date_column])

        # Step 3: Partition the data by Year
        for year, partition_df in df.groupby(df[date_column].dt.year):
            
            # Create partition path based on Year
            partition_folder = f"Year={year}/"

            # Ensure each file within the partition is uniquely named
            parquet_file_key = f"{partition_folder}data_{partition_df.index[0]}.parquet"
            
            s3_parquet_path = f"s3://{bucket_name}/{parquet_file_key}"

            # Convert the partitioned DataFrame to Parquet format
            table = pa.Table.from_pandas(partition_df)
            buffer = io.BytesIO()
            pq.write_table(table, buffer)
            buffer.seek(0)

            # Upload the Parquet file to the partitioned S3 path
            s3.upload_fileobj(buffer, bucket_name, parquet_file_key)
            print(f"Converted and uploaded Parquet file to {s3_parquet_path}.")

        print("All partitioned Parquet files uploaded successfully.")
        return True

    except Exception as e:
        print(f"Failed to convert and upload {flat_file_key}: {e}")
        return False


# Example usage
bucket_name = "flat-file-to-parquet-with-prefixes"
flat_file_key = "flat_files/generated_mock_data2.csv"
date_column = "Date"

# Call the function to convert the CSV and upload Parquet files partitioned by date
convert_flat_file_to_parquet_partitioned_by_date(bucket_name, flat_file_key, date_column)

