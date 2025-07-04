import re

def aggregate(rows: list, aggregation_expr: str) -> list:
    match = re.match(r'^(\w+)\s*=\s*(avg|min|max)$', aggregation_expr, re.IGNORECASE)
    if not match:
        raise ValueError("Aggregate must be in format: column=avg | column=min | column=max")

    col, func = match.groups()
    func = func.lower()

    if col not in rows[0]:
        raise ValueError(f"Column '{col}' not found.")

    values = [float(r[col]) for r in rows]
    if not values:
        raise ValueError("No data to aggregate.")

    result = {
        'avg': sum(values) / len(values),
        'min': min(values),
        'max': max(values)
    }[func]

    return [{'column': col, 'function': func, 'result': round(result, 2)}]
