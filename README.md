# Meesho Reseller Growth & Alert Intelligence Pipeline

## Overview

This project implements an end-to-end reseller growth monitoring pipeline for a simulated Meesho reseller business.

The workflow consists of four stages:

1. SQL Business Analytics
2. Growth Detection & Validation Engine
3. Narrative Generation & Privacy Protection
4. Agent Workflow Simulation

The pipeline transforms raw reseller and order data into validated business insights and stakeholder-ready outputs.

---

## No API Keys Required

This project runs completely offline.

No API keys, cloud services, hosted databases, paid subscriptions, or external AI services are required.

The entire pipeline operates using:

- Python
- SQLite
- CSV files
- Markdown
- Pytest

---

## Repository Structure

```text
meesho-pipeline/

├── README.md

├── data/
│   ├── generate_dataset.py
│   ├── orders.csv
│   ├── resellers.csv
│   └── meesho_reseller.db

├── part1_sql/
│   ├── queries.sql
│   ├── run_query1.py
│   ├── run_query2.py
│   ├── run_query3.py
│   ├── run_query4a.py
│   ├── run_query4b.py
│   ├── run_query5.py
│   └── output/

├── part2_engine/
│   ├── growth_engine.py
│   ├── test_growth_engine.py
│   └── fixtures/

├── part3_narrative/
│   ├── masking.py
│   ├── prompt_pack.md
│   ├── narrative_report.md
│   ├── test_masking.py
│   └── validate_narrative.py

└── part4_agent/
    ├── agent_spec.md
    └── mock_agent_runner.py
```

---

## Part 1: Dataset Generation

Generate the dataset using:

```powershell
python data/generate_dataset.py
```

Generated files:

```text
data/orders.csv
data/resellers.csv
data/meesho_reseller.db
```

The dataset is reproducible because a fixed random seed is used.

---

## Part 1: SQL Analytics

Move to:

```powershell
cd part1_sql
```

Run:

```powershell
python run_query1.py
python run_query2.py
python run_query3.py
python run_query4a.py
python run_query4b.py
python run_query5.py
```

Outputs:

```text
part1_sql/output/

monthly_category_revenue.csv
region_revenue.csv
top_resellers.csv
no_orders_resellers.csv
left_join_count_demo.csv
june_aov.csv
```

---

## Part 2: Growth Engine

Run tests:

```powershell
python -m pytest part2_engine/test_growth_engine.py
```

Expected:

```text
5 passed
```

Key functions:

- `mom_growth()`
- `is_flagged()`
- `validate_feed()`

---

## Part 3: Narrative Layer

Run masking tests:

```powershell
python part3_narrative/test_masking.py
```

Run narrative validation:

```powershell
python part3_narrative/validate_narrative.py
```

Expected:

```text
All masking tests passed!
All Part 3 masking validations passed!
```

Key files:

```text
prompt_pack.md
narrative_report.md
masking.py
```

---

## Part 4: Agent Workflow

Run:

```powershell
python part4_agent/mock_agent_runner.py
```

Expected output:

```json
{
    "feed_valid": true,
    "errors": [],
    "growth_pct": 77.1,
    "status": "flagged",
    "masked_id": "ALIAS-19"
}
```

---

## Workflow Mapping

### Part 1 → SQL Analytics

Generates verified business metrics from the SQLite dataset.

### Part 2 → Growth Detection

Validates data and calculates Month-on-Month growth.

### Part 3 → Narrative Generation

Transforms business metrics into stakeholder-facing narratives while masking reseller identities.

### Part 4 → Agent Workflow

Combines validation, growth analysis, privacy protection, and reporting into a single workflow.

---

## End-to-End Execution

```powershell
python data/generate_dataset.py

cd part1_sql
python run_query1.py
python run_query2.py
python run_query3.py
python run_query4a.py
python run_query4b.py
python run_query5.py

cd ..
python -m pytest part2_engine/test_growth_engine.py

python part3_narrative/test_masking.py
python part3_narrative/validate_narrative.py

python part4_agent/mock_agent_runner.py
```

---

## Testing

Growth Engine:

```powershell
python -m pytest part2_engine/test_growth_engine.py
```

Masking:

```powershell
python part3_narrative/test_masking.py
```

Narrative Validation:

```powershell
python part3_narrative/validate_narrative.py
```

Agent Runner:

```powershell
python part4_agent/mock_agent_runner.py
```

---

## References

Official documentation consulted during development:

- Python Standard Library Documentation
- sqlite3 Documentation
- csv Module Documentation
- Pytest Documentation

---

## Final Status

✅ Part 1 Completed

✅ Part 2 Completed

✅ Part 3 Completed

✅ Part 4 Completed

✅ Tests Passing

✅ No API Keys Required

✅ Public GitHub Repository Ready