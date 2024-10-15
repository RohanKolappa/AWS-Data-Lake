# S3-to-Parquet Data Lake with AWS Glue & Athena
This project builds a scalable data lake on AWS by transforming flat CSV files stored in Amazon S3 into optimized Parquet files, partitioned by year. The data lake architecture allows efficient storage and querying of large datasets using AWS Glue and Athena. Python scripts are used to read CSV files, convert them to Parquet, and store them in S3 with year-based partitions. AWS Glue Crawler is employed to catalog the data, making it available for fast, serverless querying with Athena.

Key Features:

Data Lake Architecture: Leverages Amazon S3 as a scalable, cost-effective data lake for large datasets.
CSV to Parquet Conversion: Transforms flat CSV files into Parquet format for space-efficient storage and fast querying.
Partitioning by Year: Organizes data into year-based partitions to optimize query performance in Athena.
AWS Glue Data Catalog: Automates the creation of data catalogs using Glue Crawlers, enabling schema discovery and partition management.
Query with AWS Athena: Supports fast, serverless queries on the partitioned Parquet data for analytics and reporting.
Technologies Used:

AWS Services: S3, Glue, Athena
Data Formats: CSV, Parquet
Tools: Python, Pandas, PyArrow
This project demonstrates the creation of a fully-functional data lake using AWS services, making large datasets easily accessible and optimized for big data analytics workflows.
