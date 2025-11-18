import boto3
import csv
import json  # Import json to convert the dictionary to a JSON string

# Initialize the SQS client
sqs = boto3.client('sqs')

# Function to create or retrieve the SQS queue
def create_sqs_queue(queue_name):
    try:
        # Check if the queue already exists by trying to get the queue URL
        response = sqs.get_queue_url(QueueName=queue_name)
        print(f"Queue already exists: {response['QueueUrl']}")
        return response['QueueUrl']
    except sqs.exceptions.QueueDoesNotExist:
        # If the queue does not exist, create a new one
        try:
            response = sqs.create_queue(
                QueueName=queue_name,
                Attributes={
                    'DelaySeconds': '5',                   # Delay message visibility by 5 seconds
                    'MessageRetentionPeriod': '86400'      # Retain messages for 1 day (86400 seconds)
                }
            )
            print(f"Queue created: {response['QueueUrl']}")
            return response['QueueUrl']
        except Exception as e:
            print(f"Error creating the queue: {str(e)}")
            return None

# Get or create the queue URL
queue_url = create_sqs_queue('my-new-queue')
