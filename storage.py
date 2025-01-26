def get_storage_slots(ast):
    slots = {}
    vars = [item for item in ast['body'] if item['type'] == 'variable']
    for i, v in enumerate(vars): slots[f"{i}"] = v

    # check for duplicate var names
    names = [slot['name'] for slot in slots.values()]  
    if {name for name in names if names.count(name) > 1}: raise ValueError("Duplicate variable names found")

    return slots
