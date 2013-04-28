import datetime
import csv
import json

csv_file = "massive file stringggggg"


def csv_read(csv_file):

    data = {}
    data["readings"] = []
    rows = csv_file.split("\n")
    
    weekend_count, weekend_energy = 0, 0
    weekday_count, weekday_energy = 0, 0

    for row in rows:

        row = row.split(",")
        
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
            date = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))
            
            if date.weekday() > 4:
                weekend_count += 1
                weekend_energy += float(row[4])
            else:
                weekday_count += 1
                weekday_energy += float(row[4])

            reading_dict["time"] = int(date.strftime('%s'))

            data["readings"].append(reading_dict)
    
    data["avg_weekday_energy"] = float(weekday_energy)/weekday_count
    data["avg_weekend_energy"] = float(weekend_energy)/weekend_count

    return json.dumps(data)
