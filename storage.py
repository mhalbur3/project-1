import csv
from typing import Dict

def saveToCSV(filename: str, data: Dict[str, int]) -> None:
    """Saves the vote counts to the CSV."""
    try:
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "votes"])
            writer.writerows([[name, votes] for name, votes in data.items()])
    except IOError as e:
        raise RuntimeError(f"Error: Failed to save votes {e}")
def loadFromCSV(filename: str) -> Dict[str, int]:
    """Loads the vote counts from the CSV."""
    try:
        with open(filename, mode="r", newline="") as file:
            reader = csv.DictReader(file)
            return {row["name"]: int(row["votes"]) for row in reader if "name" in row and "votes" in row}
    except FileNotFoundError:
        return {}
    except Exception as e:
        raise RuntimeError(f"Error: Failed to load votes: {e}")
