import sqlite3
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, "..", "data", "meesho_reseller.db")
output_dir = os.path.join(BASE_DIR, "output")
output_path = os.path.join(output_dir, "june_aov.csv")

os.makedirs(output_dir, exist_ok=True)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = """
SELECT
    ROUND(
        SUM(quantity * unit_price) / COUNT(*),
        2
    ) AS june_aov
FROM orders
WHERE month = 'June'
  AND status = 'Delivered';
"""

cursor.execute(query)
result = cursor.fetchone()

with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["june_aov"])
    writer.writerow(result)

conn.close()

print(f"Created: {output_path}")
print("AOV:", result[0])