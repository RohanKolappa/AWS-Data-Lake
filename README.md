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
