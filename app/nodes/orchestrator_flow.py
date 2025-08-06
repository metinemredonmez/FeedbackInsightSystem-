from app.nodes.transcribe_node import TranscribeNode
from app.nodes.rag_node import RAGNode
from app.nodes.grounding_node import GroundingNode
from app.nodes.hallucination_checker_node import HallucinationCheckerNode
from app.nodes.a2a_orchestration_node import A2AOrchestrationNode
from app.nodes.speak_node import SpeakNode
from app.core.config import OPENAI_API_KEY

class OrchestratorFlow:
    def __init__(self):
        self.transcriber = TranscribeNode(api_key=OPENAI_API_KEY)
        self.rag = RAGNode()
        self.grounding = GroundingNode()
        self.hallucination_checker = HallucinationCheckerNode()
        self.a2a_orchestration = A2AOrchestrationNode()
        self.speaker = SpeakNode()

    def run(self, audio_file_path: str):
        transcript = self.transcriber.run(audio_file_path)
        rag_data = self.rag.run(transcript['transcribed_text'])
        grounding_result = self.grounding.run(transcript['transcribed_text'])
        hallucinations = self.hallucination_checker.run(
            transcript['transcribed_text'],
            grounding_result['grounding_matches']
        )

        agents_outputs = {
            "transcript": transcript['transcribed_text'],
            "retrieved_docs": rag_data['retrieved_docs'],
            "grounding_matches": grounding_result['grounding_matches'],
            "hallucinations": hallucinations['hallucinated_segments']
        }

        orchestrated_result = self.a2a_orchestration.run(agents_outputs)
        spoken_response = self.speaker.run(str(orchestrated_result))

        return {
            "orchestration": orchestrated_result,
            "spoken_output": spoken_response
        }
