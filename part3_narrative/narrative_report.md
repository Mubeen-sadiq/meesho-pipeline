# Reseller Growth Narrative Report

## 1. Worked Narrative — May Ethnic Wear

### Context

**Fact:** This narrative compares Ethnic Wear revenue from April to May.

April revenue was INR 104520.77 and May revenue was INR 185107.61.

### Insight

**Fact:** Ethnic Wear revenue increased by **77.1% month over month** from April to May. The category was flagged by the Part 2 growth rule because the absolute MoM movement exceeded the 8% threshold.

### Implication

**Hypothesis:** The increase may indicate stronger demand or increased reseller activity for Ethnic Wear in May. The regional manager should check May Ethnic Wear order volume and reseller activity by region to identify where the increase occurred and whether the movement was broad-based.

### Refinement Checklist

- **Specificity:** Pass — the narrative names Ethnic Wear, April, May, and the exact 77.1% MoM movement.
- **Audience fit:** Pass — the narrative is written for a regional manager and focuses on a business action rather than technical implementation details.
- **Completeness:** Pass — the narrative contains Context, Insight, and Implication sections.
- **Actionability:** Pass — the next step is to examine May Ethnic Wear order volume and reseller activity by region.

---

## 2. Worked Narrative — June Ethnic Wear

### Context

**Fact:** This narrative compares Ethnic Wear revenue from May to June.

May revenue was INR 185107.61 and June revenue was INR 76371.53.

### Insight

**Fact:** Ethnic Wear revenue decreased by **58.74% month over month** from May to June. The category was flagged because the absolute MoM movement exceeded the 8% threshold.

### Implication

**Hypothesis:** The decrease may indicate weaker demand or reduced reseller activity for Ethnic Wear in June. The regional manager should compare June Ethnic Wear order volume and reseller activity with May, particularly by region, to determine where the decline occurred.

### Refinement Checklist

- **Specificity:** Pass — the narrative names Ethnic Wear, May, June, and the exact -58.74% MoM movement.
- **Audience fit:** Pass — the narrative is written for a regional manager and focuses on business interpretation.
- **Completeness:** Pass — the narrative contains Context, Insight, and Implication sections.
- **Actionability:** Pass — the next step is to compare June and May Ethnic Wear order volume and reseller activity by region.

---

# 3. Chart-Choice Justification

## 3.1 Which month had the highest total revenue?

A **column chart** would be appropriate because the question compares one numerical measure, total revenue, across three months. This is a simple categorical comparison and can be communicated quickly with one bar per month. The y-axis should start at zero, the chart should avoid 3D effects, and no legend is necessary because there is only one series.

The verified monthly totals are:

- April: INR 419417.43
- May: INR 444594.25
- June: INR 398055.24

---

## 3.2 What percentage share does Ethnic Wear represent of April's total revenue?

A **pie chart** can be used to communicate the share of one category within April's total revenue because this is a part-to-whole question. Ethnic Wear contributes INR 104520.77 of April's INR 419417.43 total revenue, representing **24.92%**.

The chart should have clear labels and should avoid unnecessary visual effects. Since the question focuses on percentage composition, the part-to-whole relationship should be immediately visible.

---

## 3.3 How do the four regions compare on total revenue?

A **column chart** would be appropriate because the question compares total revenue across four regions. This is a categorical comparison of one numerical measure, so the chart should contain one column for each region.

The verified regional revenues are:

- North: INR 337125.46
- South: INR 316736.68
- East: INR 275098.45
- West: INR 333106.33

The y-axis should start at zero so that the differences in revenue are represented clearly. A legend is unnecessary because there is only one series.

---

# 4. Top-Reseller Narrative With Masking

The top-reseller SQL analysis identifies five resellers whose total spend exceeded INR 50000.

For external-facing narrative purposes, raw reseller names must not be exposed. The reseller should therefore be referenced using its region and coded alias.

### Example

**Fact:** The West region includes reseller **ALIAS-19**, whose verified total spend was INR 75295.09.

**Hypothesis:** The regional manager should review the activity associated with ALIAS-19 to understand the factors contributing to the high spend and determine whether similar activity exists among other resellers in the region.

The raw reseller name is intentionally omitted from this narrative and replaced with the coded alias.

---

# 5. Narrative Validation

The narrative should satisfy the following controls:

- All numerical figures must trace to verified Part 1 or Part 2 outputs.
- May Ethnic Wear must use exactly **77.1%**.
- June Ethnic Wear must use exactly **-58.74%**.
- Facts and hypotheses must be clearly distinguished.
- Recommendations must contain a concrete next step.
- Raw reseller names must not appear in an external-facing narrative.
- Reseller identities must use the masking function from `masking.py`.