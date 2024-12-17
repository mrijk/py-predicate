def set_to_str(v: set) -> str:
    # TODO: truncate if too many items.
    items = ", ".join(str(item) for item in v)
    return f"{{{items}}}"
