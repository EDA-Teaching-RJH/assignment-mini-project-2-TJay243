# file_handler.py
import csv
from task import Task

DATA_FILE = 'tasks.csv'

def load_tasks():
    tasks = []
    try:
        with open(DATA_FILE, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tasks.append(Task(row['Title'], row['Description'], row['Deadline']))
    except FileNotFoundError:
        print("Data file not found. Starting fresh.")
    return tasks

def save_tasks(tasks):
    with open(DATA_FILE, 'w', newline='') as file:
        fieldnames = ['Title', 'Description', 'Deadline', 'Created At']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                'Title': task.title,
                'Description': task.description,
                'Deadline': task.deadline,
                'Created At': task.created_at
            })

