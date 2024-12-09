#task.py
from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def is_due(self):
        due_date = datetime.strptime(self.deadline, "%Y-%m-%d")
        return datetime.now() > due_date

    def __str__(self):
        status = "Overdue" if self.is_due() else "Upcoming"
        return f"[{status}] {self.title} - Due: {self.deadline}"
