import json

def load_grounding_data(file_path: str):
    with open(file_path, 'r') as f:
        return json.load(f)

def grounding_check(statement: str, grounding_data: dict):
    matches = [fact for fact in grounding_data.get("facts", []) if fact.lower() in statement.lower()]
    return matches if matches else ["No match found"]
