from masking import alias_for, assert_no_raw_names_leak


# Test 1: RS019 should become ALIAS-19
assert alias_for("RS019") == "ALIAS-19"


# Test 2: Raw reseller name should be detected
text_with_raw_name = "Mumbai Reseller 1 had strong growth."

assert (
    assert_no_raw_names_leak(
        text_with_raw_name,
        ["Mumbai Reseller 1"]
    )
    is False
)


# Test 3: Alias should be allowed
safe_text = "West region reseller ALIAS-19 had strong growth."

assert (
    assert_no_raw_names_leak(
        safe_text,
        ["Mumbai Reseller 1"]
    )
    is True
)

print("All masking tests passed!")