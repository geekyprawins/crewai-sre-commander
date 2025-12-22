"""
Log Analysis Agent
Responsible for analyzing log data to identify patterns and anomalies
"""

from crewai import Agent
from llm_config import get_llm


def create_log_analysis_agent() -> Agent:
    """Create the Log Analysis Agent"""
    return Agent(
        role="Log Analysis Expert",
        goal="Analyze log data to identify error patterns, anomalies, and potential root causes",
        backstory="""You are a log analysis specialist with deep expertise in parsing
        and interpreting application logs, system logs, and error traces. You can quickly
        identify patterns in log data that indicate specific failure modes, performance
        issues, or security concerns. You understand log correlation across distributed systems.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )