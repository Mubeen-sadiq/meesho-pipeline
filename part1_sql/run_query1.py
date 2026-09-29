# import sqlite3
# import csv
# db_path = "../Data/meesho_reseller.db"
# output_path = "output/monthly_category_revenue.csv"
# conn = sqlite3.connect(db_path)
# cursor = conn.cursor()
# query = """
# SELECT
#     month,
#     category,
#     ROUND(SUM(quantity * unit_price), 2) AS revenue,
#     COUNT(*) AS n_orders
# FROM orders
# GROUP BY
#     month,
#     category
# ORDER BY
#     CASE month
#         WHEN 'April' THEN 1
#         WHEN 'May' THEN 2
#         WHEN 'June' THEN 3
#     END,
#     category;
# """
# cursor.execute(query)
# rows = cursor.fetchall()
# with open(output_path, "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     writer.writerow([
#         "month",
#         "category",
#         "revenue",
#         "n_orders"
#     ])
#     writer.writerows(rows)
# conn.close()
# print(f"Created: {output_path}")
# print(f"Rows written: {len(rows)}")
import sqlite3
import csv
import os

# Get the directory where this script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build absolute paths
db_path = os.path.join(BASE_DIR, "..", "Data", "meesho_reseller.db")
output_dir = os.path.join(BASE_DIR, "output")
output_path = os.path.join(output_dir, "monthly_category_revenue.csv")

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Connect to database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query
query = """
SELECT
    month,
    category,
    ROUND(SUM(quantity * unit_price), 2) AS revenue,
    COUNT(*) AS n_orders
FROM orders
GROUP BY
    month,
    category
ORDER BY
    CASE month
        WHEN 'April' THEN 1
        WHEN 'May' THEN 2
        WHEN 'June' THEN 3
    END,
    category;
"""

# Execute query
cursor.execute(query)
rows = cursor.fetchall()

# Write results to CSV
with open(output_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow([
        "month",
        "category",
        "revenue",
        "n_orders"
    ])

    writer.writerows(rows)

# Cleanup
conn.close()

print(f"Database: {db_path}")
print(f"Created: {output_path}")
print(f"Rows written: {len(rows)}")