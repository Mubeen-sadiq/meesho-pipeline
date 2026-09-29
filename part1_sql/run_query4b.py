import sqlite3
import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, "..", "data", "meesho_reseller.db")
output_dir = os.path.join(BASE_DIR, "output")
output_path = os.path.join(output_dir, "left_join_count_demo.csv")

os.makedirs(output_dir, exist_ok=True)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = """
SELECT
    r.reseller_id,
    COUNT(*) AS count_star,
    COUNT(o.order_id) AS count_order_id
FROM resellers r
LEFT JOIN orders o
    ON r.reseller_id = o.reseller_id
WHERE r.reseller_id = 'RS024'
GROUP BY r.reseller_id;
"""

cursor.execute(query)
rows = cursor.fetchall()

with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "reseller_id",
        "count_star",
        "count_order_id"
    ])

    writer.writerows(rows)

conn.close()

print(f"Created: {output_path}")
print(f"Rows written: {len(rows)}")