import operator
import re

def apply_filter(rows: list, condition: str) -> list:
    match = re.match(r'^(\w+)\s*(=|<|>)\s*(.+)$', condition)
    if not match:
        raise ValueError("Filter must be in format: column=value or column>value")

    col, op, val = match.groups()
    if col not in rows[0]:
        raise ValueError(f"Column '{col}' not found.")

    ops = {'=': operator.eq, '<': operator.lt, '>': operator.gt}

    try:
        val = float(val)
        return [r for r in rows if ops[op](float(r[col]), val)]
    except ValueError:
        return [r for r in rows if ops[op](r[col], val)]
