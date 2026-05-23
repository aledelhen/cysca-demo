def table_to_dicts(table):
    headers = [str(cell) for cell in table.headers]
    rows = []
    for row in table.rows:
        rows.append({headers[i]: str(cell) for i, cell in enumerate(row)})
    return rows


def table_to_key_values(table, key_field="key", value_field="value"):
    return {row[key_field]: row[value_field] for row in table_to_dicts(table)}
