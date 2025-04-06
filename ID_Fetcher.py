import os
import csv
import requests

# Get script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# File paths
input_path = os.path.join(script_dir, "input.txt")
output_path = os.path.join(script_dir, "output.csv")

# Function to get the typeID from the API
def get_typeID(item_name):
    url = f"https://www.fuzzwork.co.uk/api/typeid2.php?typename={item_name}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()  # Parse the JSON response
        if data:  # If the list is not empty
            return data[0]["typeID"]
        else:
            return None  # Return None if no matching data found
    except requests.RequestException as e:
        print(f"Error fetching typeID for {item_name}: {e}")
        return None  # Return None in case of an error

# Read from input.txt
with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Prepare the data
items = []
for line in lines:
    parts = line.strip().split('\t')
    if len(parts) >= 2:
        name = parts[0].strip()
        amount = parts[1].strip()
        typeID = get_typeID(name)  # Get typeID for the item
        items.append((name, amount, typeID))  # Name = Column A, Amount = Column B, typeID = Column C

# Write to output.csv with semicolon delimiter
with open(output_path, "w", newline='', encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(["Name", "Amount", "TypeID"])  # Added TypeID column
    writer.writerows(items)

print("✅ output.csv created next to the script with Name in Column A, Amount in Column B, and TypeID in Column C.")
