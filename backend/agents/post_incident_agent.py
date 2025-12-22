"""
Post-Incident Report Agent
Responsible for generating comprehensive post-incident reports
"""

from crewai import Agent
from llm_config import get_llm


def create_post_incident_agent() -> Agent:
    """Create the Post-Incident Report Agent"""
    return Agent(
        role="Post-Incident Report Specialist",
        goal="Generate comprehensive post-incident reports with timeline, impact, and lessons learned",
        backstory="""You are a technical writer and incident management expert who
        specializes in creating detailed post-incident reports. You excel at documenting
        incident timelines, impact analysis, root cause details, and actionable lessons
        learned. Your reports help teams improve their systems and prevent similar
        incidents in the future. You write clear, structured reports for both technical
        and executive audiences.""",
        verbose=True,
        allow_delegation=False,
        llm=get_llm()
    )