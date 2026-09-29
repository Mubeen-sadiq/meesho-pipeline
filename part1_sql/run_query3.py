import sqlite3
import csv
import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
db_path = os.path.join(BASE_DIR, "..", "data", "meesho_reseller.db")
output_dir = os.path.join(BASE_DIR, "output")
output_path = os.path.join(output_dir, "top_resellers.csv")

# Ensure output folder exists
os.makedirs(output_dir, exist_ok=True)

# Connect to database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = """
SELECT
    r.reseller_id,
    r.reseller_name,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS total_spend
FROM orders o
JOIN resellers r
    ON o.reseller_id = r.reseller_id
GROUP BY
    r.reseller_id,
    r.reseller_name
HAVING
    total_spend > 50000
ORDER BY
    total_spend DESC
LIMIT 5;
"""

cursor.execute(query)
rows = cursor.fetchall()

with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "reseller_id",
        "reseller_name",
        "total_spend"
    ])

    writer.writerows(rows)

conn.close()

print(f"Created: {output_path}")
print(f"Rows written: {len(rows)}")