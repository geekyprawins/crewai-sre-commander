"""
Root Cause Analysis Agent
Responsible for synthesizing all data to determine the most likely root cause
"""

from crewai import Agent
from llm_config import get_llm


def create_root_cause_agent() -> Agent:
    """Create the Root Cause Analysis Agent"""
    return Agent(
        role="Root Cause Analysis Expert",
        goal="Synthesize all available data to determine the most likely root cause of the incident",
        backstory="""You are a senior SRE and incident commander with exceptional
        analytical skills. You excel at synthesizing information from multiple sources
        (alerts, logs, metrics, historical data) to identify the true root cause of
        complex incidents. You use systematic debugging methodologies and can distinguish
        between symptoms and actual causes. You provide evidence-based conclusions.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )