import json
import csv

with open ("health_scvs.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    data = {"name": []}
    for row in reader:
        data["name"].append({"name":
        row[0], "website": row[1]})
    print(data)