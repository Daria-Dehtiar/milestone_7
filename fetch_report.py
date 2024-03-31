import requests

def fetch_report(month, department, endpoint):
    url = f"http://127.0.0.1:5000/{endpoint}?month={month}&department={department}"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Error: Failed to fetch report. Status code: {response.status_code}"

    else:
        data = response.json()
        total = data["total"]
        employees = data["employees"]

        report = f"Report for {department} department for {month} fetched.\nTotal: {total}\nEmployees:\n"

        for employee in employees:
            if "birthday" in employee:
                date = employee["birthday"]

            elif "anniversary" in employee:
                date = employee["anniversary"]

            name = employee["name"]
            report += f"- {date}, {name}\n"

    return report

if __name__ == "__main__":
    print(fetch_report("january", "human resources","birthdays" ))
    print(fetch_report("january", "human resources","anniversaries"))


