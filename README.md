# S3-to-Parquet Data Lake with AWS Glue, Athena, and SQS for Real-time Processing
This project implements a scalable data lake on AWS by transforming flat CSV files stored in Amazon S3 into optimized Parquet files, partitioned by year, with a real-time data ingestion pipeline using Amazon SQS for batch processing. The architecture supports efficient storage, cost optimization, and fast querying of large datasets using AWS Glue and Athena. Python scripts are used to read CSV files, convert them to Parquet, and store them in S3 with year-based partitions. AWS Glue Crawlers automatically catalog the data, making it available for serverless querying with Athena.

Key Features:

- Data Lake Architecture: Utilizes Amazon S3 as a scalable, cost-effective data lake to store large datasets in a space-optimized manner.
- Real-time Data Pipeline with SQS: Amazon SQS is used to manage the flow of data in real-time. Messages are stored in memory until the batch capacity is reached, triggering the creation of Parquet files and uploading them to S3. A visibility timeout is employed to temporarily silence the message rather than delete it, limiting the number of SQS operations and reducing costs.
C- SV to Parquet Conversion: Transforms flat CSV files into Parquet format, which provides columnar storage for faster query performance and smaller storage size compared to traditional row-based formats like CSV.
- Partitioning by Year: Data is organized into year-based partitions to optimize query performance in Athena, improving search efficiency.
- AWS Glue Data Catalog: AWS Glue Crawlers automatically discover schema and partitions, making the data easily searchable and queryable through the Glue Data Catalog.
- Fast Querying with AWS Athena: Athena enables serverless, real-time queries on the partitioned Parquet data, supporting analytics and reporting at scale.
- Cost Optimization:
  - Reduced SQS Operations: By temporarily silencing (instead of deleting) messages during processing, the system reduces the number of operations on SQS, helping to lower costs.
  - Efficient Storage and Querying with Parquet: Parquet’s columnar format reduces storage size and boosts query performance compared to row-based formats, leading to faster search times and reduced computational overhead.

- Technologies Used:
    - AWS Services: S3, Glue, Athena, SQS
    - Data Formats: CSV, Parquet
    - Tools: Python, Pandas, PyArrow


This project demonstrates the creation of a highly efficient data lake with a real-time data ingestion pipeline, cost optimization, and fast query capabilities through the use of Parquet and AWS Athena, all while minimizing operational overhead with SQS.


Implements Kappa Architecture

We are also doing the following:

For sqs_to_s3:
Taking SQS messages from populated queue and writing each row/message to S3 in parquet format. To improve the current process, I am looking to extend the functionality by adding event-based triggers and batch processing. I want to process the rows, store the output in memory (using a dictionary that will be converted to a pandas df and then to a parquet file), and use visibility timeouts. Also looking to batch the delete process (instead of deleting each message one by one) using a helper function in order to limit the number of api calls.

For s3_write_parquet:
Optimized the core logic to reduce the number of API calls and S3 requests, leading to lower operational costs. Implemented batch processing, storing 1000 rows at a time before converting them into a Pandas DataFrame and writing the data in Parquet format to S3. Integrated visibility timeouts to avoid immediate deletion of SQS messages, allowing other consumers to process the same messages after a set period. This change ensures efficient message processing while maintaining message availability for other consumers.

for s3_flat_to_parquet_diff_prefix:
I have implemented a process to convert flat files stored in S3 into Parquet format, and upload them back to S3 using Pandas, Boto3, and the s3fs library. The current functionality handles entire files at once, and I am looking to enhance it by adding chunked processing, where each chunk of the file is processed and saved as an individual Parquet file. Additionally, I am exploring a cleaner approach for uploading data back to S3, beyond the current method of using upload_fileobj from Boto3.

for sqs_queue_insert:
We are able to successfully populate an SQS queue using each row from a selected flat file (csv).

<img width="1440" alt="image" src="https://github.com/user-attachments/assets/4dd631d2-0a7d-4bad-88ce-6d269888cc72">

<img width="1281" alt="image" src="https://github.com/user-attachments/assets/21f5743f-5c6a-4ad2-a9b0-9c52475488b5">





