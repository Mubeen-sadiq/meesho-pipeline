import sqlite3
import csv
import os

# Base directory of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths
db_path = os.path.join(BASE_DIR, "..", "data", "meesho_reseller.db")
output_dir = os.path.join(BASE_DIR, "output")
output_path = os.path.join(output_dir, "region_revenue.csv")

# Ensure output folder exists
os.makedirs(output_dir, exist_ok=True)

# Connect to database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

query = """
SELECT
    r.region,
    ROUND(SUM(o.quantity * o.unit_price), 2) AS revenue,
    COUNT(*) AS n_orders
FROM orders o
JOIN resellers r
    ON o.reseller_id = r.reseller_id
GROUP BY r.region
ORDER BY revenue DESC;
"""

cursor.execute(query)
rows = cursor.fetchall()

# Write CSV
with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "region",
        "revenue",
        "n_orders"
    ])

    writer.writerows(rows)

conn.close()

print(f"Created: {output_path}")
print(f"Rows written: {len(rows)}")