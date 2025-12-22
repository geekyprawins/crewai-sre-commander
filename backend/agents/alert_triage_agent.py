"""
Alert Triage Agent
Responsible for initial alert assessment and severity classification
"""

from crewai import Agent
from llm_config import get_llm


def create_alert_triage_agent() -> Agent:
    """Create the Alert Triage Agent"""
    return Agent(
        role="Alert Triage Specialist",
        goal="Analyze incoming alerts and classify their severity and urgency",
        backstory="""You are an experienced SRE with 10+ years in incident response.
        You excel at quickly assessing alerts to determine their business impact and urgency.
        You understand the difference between symptoms and root causes, and can prioritize
        multiple alerts based on service criticality and user impact.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )