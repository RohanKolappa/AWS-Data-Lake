import boto3
import csv
sqs = boto3.client('sqs')

#function to create sqs queue
def create_sqs_queue(queue_name):
	try:
		response = sqs.create_queue(QueueName=queue_name, Attributes={'DelaySeconds': '5', 'MessageRetentionPeriod': '86400'})

		print(f"Queue created: {response['QueueUrl']}")
		return response['QueueUrl']

	except Exception as e:
		print(f"Error creating the queue: {str(e)}")

queue_url = create_sqs_queue('my-new-queue')




def send_messages_to_sqs(csv_file):
	with open(csv_file, newline='') as file:
		reader = csv.DictReader(file)
		for row in reader:
			message_body = str(row)
			
			response = sqs.send_message(QueueUrl=queue_url, MessageBody=message_body)
			print(f"Sent message ID: {response['MessageId']}")

send_messages_to_sqs('diff_types_mock.csv')


