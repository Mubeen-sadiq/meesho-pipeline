import json
import os
import sys

# Project root
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

# Add project root to Python path
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

# Imports from Part 2
from part2_engine.growth_engine import (
    validate_feed,
    mom_growth,
    is_flagged,
)

# Imports from Part 3
from part3_narrative.masking import alias_for


def main():
    # Path to monthly revenue feed
    feed_path = os.path.join(
        PROJECT_ROOT,
        "part2_engine",
        "fixtures",
        "monthly_category_revenue.csv"
    )

    # Validate feed
    valid, errors = validate_feed(feed_path)

    # Sample growth calculation
    growth_pct = mom_growth(
        104520.77,
        185107.61
    )

    # Determine status
    status = is_flagged(growth_pct)

    # Mask reseller ID
    masked_id = alias_for("RS019")

    # Agent output
    result = {
        "feed_valid": valid,
        "errors": errors,
        "growth_pct": growth_pct,
        "status": status,
        "masked_id": masked_id
    }

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()