# Agent Specification

## Purpose

The agent automates revenue-feed validation, growth analysis, anomaly detection, and executive reporting for the reseller business dataset.

---

## Inputs

The agent receives:

- monthly_category_revenue.csv
- Growth threshold (default = 8%)
- Revenue and order metrics

---

## Processing Flow

### Step 1: Feed Validation

The agent validates the input feed using:

```python
validate_feed()
```

Checks performed:

- Missing category
- Missing revenue
- Non-numeric revenue
- Negative revenue

If validation fails, the workflow stops and returns validation errors.

---

### Step 2: Growth Calculation

The agent calculates Month-on-Month (MoM) growth using:

```python
mom_growth(previous, current)
```

Formula:

Growth % = ((Current - Previous) / Previous) × 100

Rounded to 2 decimal places.

---

### Step 3: Threshold Evaluation

Growth percentages are evaluated using:

```python
is_flagged()
```

Rules:

| Condition | Result |
|-----------|----------|
| abs(growth) > 8 | flagged |
| abs(growth) < 8 | not_flagged |
| abs(growth) = 8 | escalate_exact_boundary |

---

### Step 4: Narrative Generation

The agent generates a business summary including:

- Growth observations
- Key category movements
- Risks
- Recommendations

The narrative is designed for executive stakeholders.

---

### Step 5: Privacy Protection

Before producing final outputs, reseller information is masked using:

```python
mask_reseller_id()
```

Example:

RS019 → RS***

This prevents exposure of identifiable reseller information.

---

## Outputs

The agent produces:

### Validation Result

```json
{
  "feed_valid": true
}
```

### Growth Analysis

```json
{
  "growth_pct": 77.10,
  "status": "flagged"
}
```

### Masked Output

```json
{
  "masked_id": "RS***"
}
```

### Executive Narrative

Business summary with recommendations and risk indicators.

---

## Failure Handling

### Validation Failure

The agent returns:

- Missing category error
- Missing revenue error
- Negative revenue error
- Non-numeric revenue error

Processing stops until issues are corrected.

### Boundary Case

If a growth value is exactly 8%, the agent returns:

```text
escalate_exact_boundary
```

for manual review.

---

## Agent Workflow Diagram

Input CSV
↓
validate_feed()
↓
mom_growth()
↓
is_flagged()
↓
mask_reseller_id()
↓
Executive Narrative
↓
JSON Output