import json, sys, os
from datetime import datetime, timedelta

FROM, TO, TIME, DATE = sys.argv[1:]

FILE = "data.json"

if os.path.exists(FILE):
    with open(FILE) as f:
        data = json.load(f)
else:
    data = {}

key = f"{FROM} -> {TO}"

data.setdefault(DATE, {})
data[DATE].setdefault(key, {})
data[DATE][key][TIME] = data[DATE][key].get(TIME, 0) + 1

# Keep only last 5 days
today = datetime.strptime(DATE, "%Y-%m-%d")
valid_days = {
    (today - timedelta(days=i)).strftime("%Y-%m-%d")
    for i in range(5)
}

data = {d: data[d] for d in data if d in valid_days}

with open(FILE, "w") as f:
    json.dump(data, f, indent=2)
