import datetime
import calendar
import csv
import sys
import json

csv_file = "sample.csv"
data = {}
data["readings"] = []

cr = csv.reader(open(csv_file,"rb"))

for row in cr:

    if row and row[0].lower() in ["name", "address", "account number"]:
        data[row[0].lower()] = row[1]
        continue
    
    if row and row[0].lower() == "type":
        continue

    if len(row) > 5:
        reading_dict = {}
        reading_dict["date"] = row[1]
        reading_dict["start"] = row[2]
        reading_dict["end"] = row[3]
        reading_dict["kWh"] = float(row[4])
        reading_dict["type"] = row[0]
        
        month, day, year = row[1].split("/")
        hour, minute = row[2].split(":")

        reading_dict["time"] = int(datetime.datetime(int(year), int(month), int(day), int(hour), int(minute)).strftime('%s'))

        data["readings"].append(reading_dict)

print(json.dumps(data))
