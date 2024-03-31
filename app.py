from flask import Flask, request, jsonify
from data_base import data_base

app = Flask(__name__)

@app.route("/birthdays", methods=["GET"])
def get_birthdays():
    month = request.args.get("month")
    department = request.args.get("department")

    if not month or not department:
        return jsonify({"error": "Month and department parameters are required."}), 400

    DB = data_base.create_DB("data_base/employees.csv")
    filtered_records = data_base.filter_birthdays(DB, month, department)

    return jsonify({"total": len(filtered_records), "employees": filtered_records})


@app.route("/anniversaries", methods=["GET"])
def get_anniversaries():
    month = request.args.get("month")
    department = request.args.get("department")

    if not month or not department:
        return jsonify({"error": "Month and department parameters are required."}), 400

    DB = data_base.create_DB("data_base/employees.csv")
    filtered_records = data_base.filter_anniversaries(DB, month, department)

    return jsonify({"total": len(filtered_records), "employees": filtered_records})


if __name__ == "__main__":
    app.run(debug=True)






