import boto3
import csv
import json  # Import json to convert the dictionary to a JSON string
from create_queue import create_sqs_queue

# Initialize the SQS client
sqs = boto3.client('sqs')

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
send_messages_to_sqs('generated_mock_data.csv')

