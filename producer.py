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

# Function to send messages to SQS from a CSV file
def send_messages_to_sqs(csv_file):
    if queue_url is None:
        print("Queue creation failed. Exiting.")
        return

    # Open CSV file and send each row as a message to SQS
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert the row (which is a dictionary) to a JSON string
            message_body = json.dumps(row)
            
            # Send the message to SQS
            response = sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=message_body
            )
            print(f"Sent message ID: {response['MessageId']}")

# Call the function to send messages to SQS
send_messages_to_sqs('diff_types_mock.csv')

