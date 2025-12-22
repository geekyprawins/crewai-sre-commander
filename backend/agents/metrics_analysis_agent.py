"""
Metrics Analysis Agent
Responsible for analyzing system metrics and performance data
"""

from crewai import Agent
from llm_config import get_llm


def create_metrics_analysis_agent() -> Agent:
    """Create the Metrics Analysis Agent"""
    return Agent(
        role="Metrics Analysis Specialist",
        goal="Analyze system metrics to identify performance bottlenecks and resource constraints",
        backstory="""You are a performance engineering expert with extensive experience
        in system monitoring and metrics analysis. You can interpret CPU, memory, disk,
        network, and application metrics to identify performance issues, capacity problems,
        and resource exhaustion scenarios. You understand how different metrics correlate
        and can spot trends that indicate impending failures.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )