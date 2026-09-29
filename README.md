# Meesho Sales Analytics and Narrative Pipeline

## 1. Project Overview

This project is an end-to-end data analytics pipeline built around a simulated Meesho reseller and order dataset.

The project starts with raw order and reseller data and takes it through data generation, SQL analysis, business metrics, growth analysis, narrative generation, privacy masking, and final validation.

The main objective is to demonstrate how business data can be transformed into useful insights through a structured and testable workflow.

### Project flow

Data Generation
      ↓
SQLite + CSV Data
      ↓
SQL Analysis
      ↓
Business Metrics
      ↓
Growth Analysis
      ↓
Privacy Masking
      ↓
Narrative Report
      ↓
Agent Validation
```

---

# 2. Objectives

The project was developed with the following objectives:

- Create a realistic business dataset for reseller and order analysis.
- Store the generated data in CSV files and a SQLite database.
- Use SQL to answer practical business questions.
- Generate reusable analytical output files.
- Calculate growth and business performance metrics.
- Protect reseller identifiers before using them in narrative output.
- Convert analytical findings into a readable business narrative.
- Validate the narrative input using a mock agent workflow.
- Add automated tests for important parts of the project.
- Maintain a clear and reproducible project structure.

---

# 3. Technologies Used

The project uses the following technologies:

| Technology | Purpose |
|---|---|
| Python | Data generation, processing, testing and validation |
| SQLite | Storing the project dataset |
| SQL | Business analysis and aggregation |
| CSV | Storing analytical outputs |
| Pytest | Automated testing |
| Markdown | Project documentation and narrative |
| VS Code | Development environment |
| Git | Version control |
| GitHub | Repository hosting and submission |

---

# 4. Project Structure

The project is organized into separate stages so that each part has a clear purpose.


meesho-pipeline/
│
├── README.md
│
├── Data/
│   ├── generate_dataset.py
│   ├── meesho_reseller.db
│   ├── orders.csv
│   └── resellers.csv
│
├── part1_sql/
│   ├── queries.sql
│   ├── run_query1.py
│   ├── run_query2.py
│   ├── run_query3.py
│   ├── run_query4a.py
│   ├── run_query4b.py
│   ├── run_query5.py
│   │
│   └── output/
│       ├── june_aov.csv
│       ├── left_join_count_demo.csv
│       ├── monthly_category_revenue.csv
│       ├── no_orders_resellers.csv
│       ├── region_revenue.csv
│       └── top_resellers.csv
│
├── part2_engine/
│   ├── growth_engine.py
│   ├── test_growth_engine.py
│   └── fixtures/
│
├── part3_narrative/
│   ├── masking.py
│   ├── test_masking.py
│   ├── prompt_pack.md
│   ├── narrative_report.md
│   └── validate_narrative.py
│
└── part4_agent/
    ├── agent_spec.md
    └── mock_agent_runner.py
```

---

# 5. Data Generation

The first stage of the project is responsible for creating the dataset.

The main script is:


Data/generate_dataset.py
```

It generates reseller and order information and stores the results in both CSV and SQLite formats.

## Run the data generation script

Open the VS Code terminal and move to the project directory:

```powershell
cd C:\Users\Lenovo\Desktop\meesho-pipeline
```

Run:

powershell
python Data/generate_dataset.py


The script generates:
Data/orders.csv
Data/resellers.csv
Data/meesho_reseller.db


The generated dataset contains:

- 24 resellers
- 900 orders
- 3 months of order data
- April, May and June
- 4 regions
- Multiple cities
- Multiple product categories
- Different order statuses
- A reseller with no orders for join and validation scenarios

The dataset generation uses a fixed random seed, which makes the generated data reproducible.

---

# 6. Dataset Details

The order dataset contains business information such as:

- Order ID
- Reseller ID
- Region
- City
- Category
- Price
- Order status
- Month
- Other order-related attributes used by the analysis

The reseller dataset contains reseller-level information used for reseller analysis.

The project uses categories including:
Ethnic Wear
Western Wear
Kids Wear
Home & Kitchen
Beauty & Personal Care


The order statuses include:

Delivered
Returned
Cancelled
Pending

The data is intentionally generated to provide different business situations that can be analyzed using SQL and Python.

---

# 7. Database

The generated SQLite database is:


Data/meesho_reseller.db


SQLite was selected because it is lightweight and does not require a separate database server for this project.

The database provides a convenient way to execute SQL queries against the generated business data.

The project also keeps the original CSV files so that the data can be inspected independently of the database.

---

# 8. Part 1 – SQL Analysis

The first analytical stage is located in:

part1_sql/

The SQL source file is:


queries.sql


The Python files are used to execute the individual analysis queries.

Current query runner files:


run_query1.py
run_query2.py
run_query3.py
run_query4a.py
run_query4b.py
run_query5.py


---

# 9. Running the SQL Analysis

From the project root:

```powershell
cd C:\Users\Lenovo\Desktop\meesho-pipeline
```

Move into the SQL folder:

```powershell
cd part1_sql
```

Run the queries one by one.

### Query 1

```powershell
python run_query1.py
```

### Query 2

```powershell
python run_query2.py
```

### Query 3

```powershell
python run_query3.py
```

### Query 4A

```powershell
python run_query4a.py
```

### Query 4B

```powershell
python run_query4b.py
```

### Query 5

```powershell
python run_query5.py
```

The analytical results are written to:


part1_sql/output/
```

---

# 10. SQL Output Files

The current output directory contains the following files.

## `monthly_category_revenue.csv`

This output is used to examine revenue across months and product categories.

It helps answer questions such as:

- Which category generated more revenue?
- How did category revenue change between months?
- Which month had stronger category performance?

---

## `region_revenue.csv`

This file contains regional revenue information.

It helps compare business performance across regions.

The project includes regions such as:


North
South
East
West


---

## `top_resellers.csv`

This file contains reseller-level performance information.

It can be used to identify resellers contributing higher revenue.

---

## `no_orders_resellers.csv`

This output identifies resellers that do not have matching orders.

This is useful for demonstrating the difference between an inner join and a left join.

It also provides a useful business scenario for identifying inactive or unused reseller records.

---

## `june_aov.csv`

This file contains Average Order Value related information for June.

AOV can be used as a simple business metric to understand the average value generated per order.

The general calculation is:

AOV = Total Revenue / Number of Orders
```

---

## `left_join_count_demo.csv`

This output demonstrates the result of a left-join based analysis.

It helps show how records from the reseller table can still appear even when there is no matching order.

---

# 11. SQL Concepts Demonstrated

The SQL section demonstrates practical SQL concepts including:

### SELECT

Used to retrieve the required columns from the tables.

### WHERE

Used to filter records according to business conditions.

### GROUP BY

Used to group data for summary calculations.

For example:
Revenue by region
Revenue by category
Revenue by month
```

### HAVING

Used to filter grouped results after aggregation.

### ORDER BY

Used to sort analytical results.

### SUM

Used for revenue calculations.

### COUNT

Used for order and reseller counts.

### AVG

Used where average-based analysis is required.

### JOIN

Used to combine information from related tables.

### LEFT JOIN

Used to retain reseller records even when they do not have matching orders.

---

# 12. Part 2 – Growth Engine

The second stage is located in:

part2_engine/

The main implementation is:
growth_engine.py
The corresponding test file is:
test_growth_engine.py

The `fixtures` directory contains supporting test data used by the test cases.

The purpose of this stage is to take analytical information and calculate business-growth related metrics.

---

# 13. Testing the Growth Engine

From the project root, run:

```powershell
pytest part2_engine/test_growth_engine.py
```

If the `pytest` command is not recognized, use:

```powershell
python -m pytest part2_engine/test_growth_engine.py
```

The test suite checks whether the growth-engine calculations behave as expected for the supplied test cases.

Testing the calculation logic separately makes it easier to identify problems before the results are used by the narrative stage.

---

# 14. Part 3 – Narrative Layer

The third stage is located in:

part3_narrative/
```

This stage converts analytical information into a business-oriented narrative.

The main files are:

masking.py
test_masking.py
prompt_pack.md
narrative_report.md
validate_narrative.py
```

Each file has a specific role.

---

# 15. Reseller ID Masking

The file:


masking.py
```

contains the reseller identifier masking logic.

The purpose of masking is to avoid directly exposing reseller identifiers in the narrative output.

The general flow is:


Original Reseller ID
        ↓
Masking Function
        ↓
Masked Reseller ID
        ↓
Narrative Report
```

For example, an original reseller identifier can be transformed into a masked representation before it is included in narrative content.

This creates a simple privacy layer between the source data and the final narrative.

---

# 16. Testing the Masking Function

Move to the narrative directory:

```powershell
cd C:\Users\Lenovo\Desktop\meesho-pipeline\part3_narrative
```

Run:

```powershell
python test_masking.py
```

The expected successful result is:

All masking tests passed!
```

The masking tests have been successfully completed in the project.

---

# 17. Prompt Pack

The file:

prompt_pack.md
```

contains the instructions and information structure used for the narrative stage.

The prompt pack helps maintain consistency when converting analytical findings into a readable business summary.

The narrative should remain connected to the actual analytical outputs rather than introducing unsupported figures or assumptions.

---

# 18. Narrative Report

The main narrative output is:


narrative_report.md
```

This report presents the findings from the analysis in a more understandable business format.

The report can cover areas such as:

- Overall revenue performance
- Monthly trends
- Category performance
- Regional performance
- Reseller performance
- Average order value
- Areas that require attention
- Business observations based on the available data

The numerical values in the narrative should correspond to the analytical CSV files generated in Part 1.

---

# 19. Narrative Validation

The file:

validate_narrative.py
```

is used to validate the narrative-related information.

Run it from:


part3_narrative
```

using:

```powershell
python validate_narrative.py
```

The validation stage helps check whether the narrative follows the expected structure and requirements.

---

# 20. Part 4 – Mock Agent

The final stage of the project is located in:

part4_agent/
```

It contains:


agent_spec.md
mock_agent_runner.py
```

This stage represents an agent-style validation workflow.

The agent specification defines what needs to be checked, while the mock runner executes the validation.

---

# 21. Agent Specification

The file:


agent_spec.md
```

describes the expected behavior of the mock agent.

It acts as the specification for the validation process.

The specification provides the rules that the mock runner follows when checking the narrative feed.

---

# 22. Running the Mock Agent

Move to the agent directory:

```powershell
cd C:\Users\Lenovo\Desktop\meesho-pipeline\part4_agent
```

Run:

```powershell
python mock_agent_runner.py
```

The successful execution currently produces:

```json
{
    "feed_valid": true,
    "errors": []
}
```

This indicates that the supplied feed passed the validation checks and that no validation errors were returned.

---

# 23. End-to-End Execution

The complete project can be executed in the following order.

## Step 1 – Open the project

```powershell
cd C:\Users\Lenovo\Desktop\meesho-pipeline
```

## Step 2 – Generate the data

```powershell
python Data/generate_dataset.py
```

## Step 3 – Run SQL Query 1

```powershell
cd part1_sql
python run_query1.py
```

## Step 4 – Run SQL Query 2

```powershell
python run_query2.py
```

## Step 5 – Run SQL Query 3

```powershell
python run_query3.py
```

## Step 6 – Run SQL Query 4A

```powershell
python run_query4a.py
```

## Step 7 – Run SQL Query 4B

```powershell
python run_query4b.py
```

## Step 8 – Run SQL Query 5

```powershell
python run_query5.py
```

## Step 9 – Return to the project root

```powershell
cd ..
```

## Step 10 – Test the growth engine

```powershell
python -m pytest part2_engine/test_growth_engine.py
```

## Step 11 – Test masking

```powershell
python part3_narrative/test_masking.py
```

Expected:

All masking tests passed!
```

## Step 12 – Validate the narrative

```powershell
python part3_narrative/validate_narrative.py
```

## Step 13 – Run the mock agent

```powershell
python part4_agent/mock_agent_runner.py
```

Expected:

```json
{
    "feed_valid": true,
    "errors": []
}
```

---

# 24. Complete Workflow

The project can be understood as five main layers.

### Layer 1 – Data


generate_dataset.py
        ↓
CSV files + SQLite database
```

### Layer 2 – SQL Analysis

SQLite database
        ↓
SQL queries
        ↓
Analytical CSV outputs
```

### Layer 3 – Business Analysis


Analytical outputs
        ↓
Growth engine
        ↓
Business metrics
```

### Layer 4 – Narrative

Business metrics
        ↓
Mask reseller identifiers
        ↓
Prompt / narrative process
        ↓
Narrative report
```

### Layer 5 – Validation


Narrative feed
        ↓
Mock agent
        ↓
Validation result
```

---

# 25. Why the Project Is Structured This Way

The project is divided into multiple parts instead of placing everything in a single Python file.

This makes the workflow easier to understand and maintain.

For example:

- Data generation is separate from analysis.
- SQL analysis is separate from Python business logic.
- Business calculations are separate from narrative generation.
- Privacy masking is handled separately.
- Testing is included alongside the relevant functionality.
- Agent validation is kept as a separate final stage.

This structure also makes it easier to replace or improve one stage without changing the entire project.

---

# 26. Reproducibility

The dataset generation script uses a fixed random seed.

This means that when the dataset is generated using the same code and configuration, the resulting dataset remains reproducible.

This is useful for testing because the SQL queries and calculations can be checked against a consistent dataset.

---

# 27. Testing Approach

Testing is included at multiple points in the pipeline.

### Growth engine

```powershell
python -m pytest part2_engine/test_growth_engine.py
```

### Masking

```powershell
python part3_narrative/test_masking.py
```

### Narrative validation

```powershell
python part3_narrative/validate_narrative.py
```

### Agent validation

```powershell
python part4_agent/mock_agent_runner.py
```

The final mock-agent validation currently returns:


feed_valid: true
errors: []
```

---

# 28. Business Questions Answered by the Project

The project is designed to support questions such as:

### Revenue

- What is the revenue generated during each month?
- How does revenue vary across categories?
- Which regions contribute to revenue?

### Category

- Which product categories generate higher revenue?
- How does category performance change over time?

### Region

- How does revenue differ between North, South, East and West?
- Which regions have higher or lower contribution?

### Reseller

- Which resellers generate higher revenue?
- Which resellers have no orders?
- How can reseller activity be compared?

### Orders

- How many orders are present?
- How are orders distributed across different statuses?
- What is the average order value for a selected period?

---

# 29. Example Analytical Outputs

The project produces the following output files:


part1_sql/output/
```
with:
june_aov.csv
left_join_count_demo.csv
monthly_category_revenue.csv
no_orders_resellers.csv
region_revenue.csv
top_resellers.csv
```

These files can be opened in Excel or another spreadsheet application for further analysis.

---

# 30. Development Environment

The project was developed using:
Operating System: Windows
Editor: Visual Studio Code
Language: Python
Database: SQLite
Testing: Pytest
Version Control: Git
Repository: GitHub
```

The commands in this README are written for the Windows PowerShell terminal used during development.

---

# 31. Troubleshooting

## Python script does not run

First confirm the current directory:

```powershell
pwd
```
For example:
C:\Users\Lenovo\Desktop\meesho-pipeline
```

Then use the path appropriate for the script.

For example:

```powershell
python Data/generate_dataset.py
```

---

## `run_query1.py` cannot be found

Make sure the terminal is inside:


C:\Users\Lenovo\Desktop\meesho-pipeline\part1_sql
```

Then run:

```powershell
python run_query1.py
```

Alternatively, from the project root:

```powershell
python part1_sql/run_query1.py
```

---

## Pytest is not recognized

Use:

```powershell
python -m pytest
```

instead of:

```powershell
pytest
```

For the growth engine:

```powershell
python -m pytest part2_engine/test_growth_engine.py
```

---

## Import error in the agent

If an import error occurs in:

part4_agent/mock_agent_runner.py
```

check that the required function exists in:

part3_narrative/masking.py
```

and that the import statement matches the actual function name.

The current version of the project has already been tested successfully after correcting the masking import issue.

---

# 32. Final Validation Checklist

Before submitting the project, verify the following.

## Data
[ ] Data/generate_dataset.py is present
[ ] Data/orders.csv is present
[ ] Data/resellers.csv is present
[ ] Data/meesho_reseller.db is present
```

## SQL

[ ] part1_sql/queries.sql is present
[ ] run_query1.py is present
[ ] run_query2.py is present
[ ] run_query3.py is present
[ ] run_query4a.py is present
[ ] run_query4b.py is present
[ ] run_query5.py is present
[ ] SQL output CSV files are present
```

## Growth Engine
[ ] growth_engine.py is present
[ ] test_growth_engine.py is present
[ ] Growth engine tests pass
```

## Narrative
[ ] masking.py is present
[ ] test_masking.py is present
[ ] Masking tests pass
[ ] prompt_pack.md is present
[ ] narrative_report.md is present
[ ] validate_narrative.py is present
```

## Agent
[ ] agent_spec.md is present
[ ] mock_agent_runner.py is present
[ ] feed_valid is true
[ ] errors list is empty
```

## Documentation
[ ] README.md is present in the project root
[ ] README explains project setup
[ ] README explains execution steps
[ ] README explains the project structure
[ ] README explains the analytical stages
```

---

# 33. Final Result

The completed workflow demonstrates how a business dataset can move through a complete analytical process:

Raw Business Data
       ↓
Data Preparation
       ↓
SQL Analysis
       ↓
Business Metrics
       ↓
Growth Analysis
       ↓
Privacy Masking
       ↓
Business Narrative
       ↓
Validation
```

The project combines data preparation, SQL, Python, testing, documentation and an agent-style validation layer into one end-to-end workflow.
