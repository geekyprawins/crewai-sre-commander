"""
Action Recommendation Agent
Responsible for recommending specific mitigation and resolution actions
"""

from crewai import Agent
from llm_config import get_llm


def create_action_recommendation_agent() -> Agent:
    """Create the Action Recommendation Agent"""
    return Agent(
        role="Action Recommendation Specialist",
        goal="Provide specific, actionable mitigation and resolution steps based on root cause analysis",
        backstory="""You are an expert incident responder with deep operational knowledge
        of system administration, application deployment, and emergency procedures. You
        provide clear, prioritized action plans that minimize downtime and prevent
        incident escalation. You understand the trade-offs between quick fixes and
        permanent solutions, and can recommend both immediate mitigation and long-term fixes.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )