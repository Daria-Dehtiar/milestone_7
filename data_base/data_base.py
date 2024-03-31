import csv
from typing import List
from datetime import datetime

def create_DB(filename: str) -> List[list]:
    _DB = []
    with open(filename) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if len(row) > 0:
                _DB.append(row)
    return _DB

def filter_birthdays(DB: List[list], month: str, department: str) -> List[dict]:
    filtered_records = []
    for row in DB:
        if row[0].lower() == department.lower() and row[2].lower().startswith(month.lower()):
            filtered_records.append({"id": DB.index(row), "name": row[1], "birthday": row[2]})
    return filtered_records

def filter_anniversaries(DB: List[list], month: str, department: str) -> List[dict]:
    filtered_records = []
    for row in DB:
        hiring_date = datetime.strptime(row[4], "%Y-%m-%d")
        if hiring_date.year == datetime.now().year:
            continue
        if row[0].lower() == department.lower() and hiring_date.strftime("%B").lower() == month.lower():
            filtered_records.append({"id": DB.index(row), "name": row[1], "anniversary": str(hiring_date.strftime("%B %d"))})
    return filtered_records