import boto3
import json
from s3_writer import S3Writer  # Ensure the S3Writer class is correctly set up
from create_queue import create_sqs_queue
# Initialize the SQS client
sqs = boto3.client('sqs')

#create queue and get url, if queue already exists then just get queue url
queue_url = create_sqs_queue('my-new-queue')

# Initialize the S3Writer
s3_writer = S3Writer()

def consume_messages():
    while True:
        # Receive messages from the queue
        response = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=10,  # Adjust batch size for how many messages you want to process at a time
            WaitTimeSeconds=20,        # Long polling for up to 20 seconds
            VisibilityTimeout=300
        )

        # Get the list of messages from the response
        messages = response.get('Messages', [])

        if messages:
            for message in messages:
                message_body = message['Body']  # The message body (typically JSON)
                try:
                    data = json.loads(message_body)  # Convert the message body from JSON string to Python dict

                    # Process the message by writing it to S3 using the S3Writer
                    s3_writer.add_row(data)


                    # Delete the message from the queue after it has been successfully processed
                    # sqs.delete_message(
                    #    QueueUrl=queue_url,
                    #    ReceiptHandle=message['ReceiptHandle']
                    #)
                    #print(f"Deleted message ID: {message['MessageId']}")
                except json.JSONDecodeError:
                    print(f"Failed to decode message: {message_body}")
        else:
            print("No messages to process.")
            break
# Start consuming messages from SQS and writing them to S3
if __name__ == '__main__':
    consume_messages()

    s3_writer.flush()
