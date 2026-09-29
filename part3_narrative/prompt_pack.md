# Reusable Prompt Pack — Reseller Growth Narrative

## Trigger

Run this prompt when a category's `is_flagged` result from Part 2 is:

`flagged`

The purpose is to convert a verified month-over-month category movement into a concise stakeholder update for a regional manager.

---

## Input list

The prompt requires the following verified input values:

- `{category}` — category name
- `{previous_revenue}` — revenue for the previous month
- `{current_revenue}` — revenue for the current month
- `{mom_pct}` — calculated month-over-month percentage
- `{month}` — current month
- `{prev_month}` — previous month
- `{n_orders_previous}` — previous-month order count
- `{n_orders_current}` — current-month order count
- `{region}` — region, when relevant
- `{reseller_alias}` — coded reseller alias, when a reseller is referenced

Only values supplied through these placeholders may appear as numerical facts in the final narrative.

---

## Prompt

Using only the verified input values supplied below, write a stakeholder update for a regional manager.

Structure the update as:

### Context
Explain what category is being measured and compare `{month}` with `{prev_month}`.

### Insight
State the verified movement using the exact supplied `{mom_pct}` value.

Label this statement explicitly as:

**Fact**

Do not invent or calculate any additional number that is not supplied in the input list.

### Implication
Give one specific and actionable next step for the regional manager.

If the recommendation proposes a possible cause that the supplied data does not prove, label it explicitly as:

**Hypothesis**

Do not present an unverified cause as a fact.

If a reseller must be mentioned, use only `{reseller_alias}` and never use the raw reseller name.

Keep the narrative concise and suitable for a regional manager rather than a technical audience.

---

## Checklist

Before the narrative is used, verify all of the following:

- [ ] Every numerical figure in the narrative matches a supplied input value exactly.
- [ ] The category name and both comparison months are stated correctly.
- [ ] The verified result is explicitly labeled as a **Fact**.
- [ ] Any proposed cause that is not proven by the data is explicitly labeled as a **Hypothesis**.
- [ ] The recommendation is specific and actionable rather than a vague instruction.
- [ ] The narrative is written for a regional manager and avoids unnecessary technical terminology.
- [ ] Any reseller reference uses the coded alias and never the raw reseller name.
- [ ] `assert_no_raw_names_leak()` returns `True` for the final narrative.