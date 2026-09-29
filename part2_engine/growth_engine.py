import csv


def mom_growth(previous: float, current: float) -> float:
    """
    Returns Month-on-Month growth percentage.
    """
    return round(((current - previous) / previous) * 100, 2)


def is_flagged(mom_pct: float, threshold: float = 8.0) -> str:
    """
    Determines whether growth should be flagged.
    """

    if abs(mom_pct) > threshold:
        return "flagged"

    if abs(mom_pct) < threshold:
        return "not_flagged"

    return "escalate_exact_boundary"


def validate_feed(csv_path: str):
    """
    Validate monthly revenue CSV feed.
    """

    errors = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for line_num, row in enumerate(reader, start=2):

            month = row["month"].strip()
            category = row["category"].strip()
            revenue = row["revenue"].strip()

            # Missing category
            if not category:
                errors.append(
                    f"line {line_num}: missing category (month={month})"
                )

            # Missing revenue
            if revenue == "":
                errors.append(
                    f"line {line_num}: missing revenue (category={category})"
                )
                continue

            # Revenue numeric?
            try:
                revenue_value = float(revenue)
            except ValueError:
                errors.append(
                    f"line {line_num}: revenue not numeric: {revenue!r}"
                )
                continue

            # Negative revenue?
            if revenue_value < 0:
                errors.append(
                    f"line {line_num}: negative revenue ({revenue_value}) "
                    f"for category={category}"
                )

    if errors:
        return False, errors

    return True, []