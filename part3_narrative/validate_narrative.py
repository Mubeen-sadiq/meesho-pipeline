from pathlib import Path

from masking import alias_for, assert_no_raw_names_leak


# --------------------------------------------------
# Test 1: Alias conversion
# --------------------------------------------------

assert alias_for("RS019") == "ALIAS-19"

print("Test 1 passed: RS019 -> ALIAS-19")


# --------------------------------------------------
# Read the final narrative
# --------------------------------------------------

report_path = Path("narrative_report.md")
narrative = report_path.read_text(encoding="utf-8")


# Raw reseller names from the Part 1 top-reseller query
reseller_names = [
    "Mumbai Reseller 1",
    "Mumbai Reseller 4",
    "Hyderabad Reseller 6",
    "Lucknow Reseller 6",
    "Jaipur Reseller 5",
]


# --------------------------------------------------
# Test 2: Final narrative must not leak raw names
# --------------------------------------------------

assert_no_leak = assert_no_raw_names_leak(
    narrative,
    reseller_names
)

assert assert_no_leak is True

print("Test 2 passed: No raw reseller names found")


# --------------------------------------------------
# Test 3: Negative case
# A narrative containing a raw name MUST fail
# --------------------------------------------------

unsafe_narrative = (
    "Mumbai Reseller 1 had strong growth."
)

assert (
    assert_no_raw_names_leak(
        unsafe_narrative,
        reseller_names
    )
    is False
)

print("Test 3 passed: Raw-name leak correctly detected")


print("All Part 3 masking validations passed!")