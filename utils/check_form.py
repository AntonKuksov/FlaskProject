def is_empty(value: str) -> bool:
    return bool(value.strip())


def is_number(value: str) -> bool:
    try:
        float(value)
        return False
    except ValueError:
        return True


