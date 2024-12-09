# utilities.py
import re
from datetime import datetime

def validate_title(title):
    return bool(re.match(r'^[a-zA-Z0-9\s]{3,50}$', title))

def validate_deadline(deadline):
    try:
        datetime.strptime(deadline, "%Y-%m-%d")
        return True
    except ValueError:
        return False
