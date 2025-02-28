import numpy as np

def evaluate_formula(formula, cell_values):
    if formula.startswith("="):
        formula = formula[1:]
        if "SUM" in formula:
            return np.sum(cell_values)
        elif "AVERAGE" in formula:
            return np.mean(cell_values)
        elif "MAX" in formula:
            return np.max(cell_values)
        elif "MIN" in formula:
            return np.min(cell_values)
        elif "COUNT" in formula:
            return len(cell_values)
    return None