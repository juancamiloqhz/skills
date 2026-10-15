def partition(values):
    result = {"negative": [], "other": []}
    for value in values:
        result["negative" if value < 0 else "other"].append(value)
    return result
