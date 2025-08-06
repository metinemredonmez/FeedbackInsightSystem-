from app.langchain_utils.langgraph_flow import run_analysis_flow

def test_analysis_flow():
    result = run_analysis_flow("The seat was uncomfortable but the crew was friendly.")
    assert "multi_agent_output" in result
    assert "grounding_check" in result
