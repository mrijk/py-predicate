def set_to_str(v: set) -> str:
    items = ", ".join(str(item) for item in v)
    return f"{{{items}}}"
