from app.langchain_utils.grounding_agent import load_grounding_data, grounding_check
import os

class GroundingNode:
    def __init__(self):
        data_path = os.path.join(os.path.dirname(__file__), '../../data/ffsdb.json')
        self.grounding_data = load_grounding_data(data_path)

    def run(self, statement: str):
        return {"grounding_matches": grounding_check(statement, self.grounding_data)}
