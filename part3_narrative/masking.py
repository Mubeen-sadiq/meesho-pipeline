def alias_for(reseller_id: str) -> str:
    """
    Convert a reseller ID such as RS019 into ALIAS-19.
    """
    number = int(reseller_id.replace("RS", ""))
    return f"ALIAS-{number}"


def assert_no_raw_names_leak(
    text: str,
    reseller_names: list[str]
) -> bool:
    """
    Return False if any raw reseller name appears in the text.
    Return True if no raw reseller name appears.
    """
    for name in reseller_names:
        if name in text:
            return False

    return True