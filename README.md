Taking SQS messages from populated queue and writing each row/message to S3 in parquet format. To improve the current process, I am looking to extend the functionality by adding event-based triggers and batch processing. I want to process the rows, store the output in memory (using a dictionary that will be converted to a pandas df and then to a parquet file), and use visibility timeouts. Also looking to batch the delete process (instead of deleting each message one by one) using a helper function in order to limit the number of api calls.


