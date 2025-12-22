"""
Knowledge Base Agent
Responsible for correlating current incident with historical incidents and known issues
"""

from crewai import Agent
from llm_config import get_llm


def create_knowledge_base_agent() -> Agent:
    """Create the Knowledge Base Agent"""
    return Agent(
        role="Knowledge Base Specialist",
        goal="Correlate current incident data with historical incidents and known patterns",
        backstory="""You are an incident management expert with comprehensive knowledge
        of past incidents, their root causes, and resolution patterns. You excel at
        pattern matching between current symptoms and historical incidents to accelerate
        diagnosis. You maintain detailed knowledge of system architecture, common failure
        modes, and proven resolution strategies.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )