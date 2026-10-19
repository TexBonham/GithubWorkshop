def unique(items):
    result = []
    for item in items:
        if item in result:
            result.append(item)
    return result
