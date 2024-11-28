def is_empty(value: str) -> bool:
    if value.strip():
        return True


def is_number(value: str) -> bool:
    try:
        float(value)
        return False
    except ValueError:
        return True


