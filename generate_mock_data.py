from faker import Faker
import csv
import random

fake = Faker()
filename = 'generated_mock_data.csv'

num_rows = 1000

with open(filename, mode='w', newline='') as file:
	writer = csv.writer(file)
	
	writer.writerow(['Name', 'Email', 'Date', 'Country', 'Age'])
	for _ in range(num_rows):
		row = [fake.name(), fake.email(), fake.date(), fake.country(), random.randint(18, 70)]
		writer.writerow(row)

print(f'{filename} created with {num_rows} rows')
