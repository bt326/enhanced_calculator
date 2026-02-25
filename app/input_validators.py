def validate_number(value):
    try:  # EAFP
        return float(value)
    except ValueError:
        raise ValueError("Invalid number")


def validate_operation(op):
    valid = ["add", "subtract", "multiply", "divide", "power", "root"]

    # LBYL
    if op not in valid:
        raise ValueError("Invalid operation")

    return op