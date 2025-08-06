class HallucinationCheckerNode:
    def run(self, text: str, known_facts: list):
        hallucinated = [phrase.strip() for phrase in text.split(".") if not any(fact.lower() in phrase.lower() for fact in known_facts)]
        return {"hallucinated_segments": hallucinated}
