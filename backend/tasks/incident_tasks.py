"""
CrewAI Tasks for Incident Analysis Pipeline
Defines the sequential tasks that agents will execute
"""

from crewai import Task
from typing import Dict, Any


def create_alert_triage_task(agent, incident_data: Dict[str, Any]) -> Task:
    """Task for initial alert triage and severity assessment"""
    return Task(
        description=f"""
        Analyze the following incident data and perform initial triage:
        
        Alert Data: {incident_data.get('alert', 'No alert data provided')}
        
        Your task is to:
        1. Assess the severity level (P0-Critical, P1-High, P2-Medium, P3-Low)
        2. Identify the primary affected services
        3. Estimate potential business impact
        4. Determine urgency level
        5. Provide initial classification
        
        Output your analysis as a JSON object with the following structure:
        {{
            "severity": "P0|P1|P2|P3",
            "urgency": "Critical|High|Medium|Low",
            "affected_services": ["service1", "service2"],
            "business_impact": "description of impact",
            "classification": "brief classification",
            "confidence": "High|Medium|Low"
        }}
        """,
        agent=agent,
        expected_output="JSON object with triage assessment"
    )


def create_log_analysis_task(agent, incident_data: Dict[str, Any]) -> Task:
    """Task for analyzing log data"""
    return Task(
        description=f"""
        Analyze the following log data to identify patterns and anomalies:
        
        Log Data: {incident_data.get('logs', 'No log data provided')}
        
        Your task is to:
        1. Identify error patterns and anomalies
        2. Extract relevant error messages and stack traces
        3. Determine timeline of events from logs
        4. Identify potential failure points
        5. Correlate log entries across services
        
        Output your analysis as a JSON object with the following structure:
        {{
            "error_patterns": ["pattern1", "pattern2"],
            "key_errors": ["error1", "error2"],
            "timeline": [
                {{"timestamp": "time", "event": "description", "severity": "level"}}
            ],
            "failure_indicators": ["indicator1", "indicator2"],
            "log_correlation": "description of correlations found"
        }}
        """,
        agent=agent,
        expected_output="JSON object with log analysis results"
    )


def create_metrics_analysis_task(agent, incident_data: Dict[str, Any]) -> Task:
    """Task for analyzing metrics data"""
    return Task(
        description=f"""
        Analyze the following metrics data to identify performance issues:
        
        Metrics Data: {incident_data.get('metrics', 'No metrics data provided')}
        
        Your task is to:
        1. Identify resource constraints and bottlenecks
        2. Analyze performance trends and anomalies
        3. Detect capacity issues
        4. Correlate metrics across services
        5. Identify threshold breaches
        
        Output your analysis as a JSON object with the following structure:
        {{
            "resource_constraints": ["constraint1", "constraint2"],
            "performance_anomalies": ["anomaly1", "anomaly2"],
            "capacity_issues": ["issue1", "issue2"],
            "threshold_breaches": [
                {{"metric": "name", "value": "current", "threshold": "limit", "severity": "level"}}
            ],
            "trends": "description of concerning trends"
        }}
        """,
        agent=agent,
        expected_output="JSON object with metrics analysis results"
    )


def create_knowledge_base_task(agent, past_incidents: list) -> Task:
    """Task for correlating with historical incidents"""
    return Task(
        description=f"""
        Correlate the current incident with historical incidents and patterns:
        
        Historical Incidents: {past_incidents}
        
        Your task is to:
        1. Find similar past incidents
        2. Identify recurring patterns
        3. Extract relevant lessons learned
        4. Suggest proven resolution strategies
        5. Highlight preventive measures that were effective
        
        Output your analysis as a JSON object with the following structure:
        {{
            "similar_incidents": [
                {{"id": "incident_id", "similarity": "description", "outcome": "resolution"}}
            ],
            "recurring_patterns": ["pattern1", "pattern2"],
            "lessons_learned": ["lesson1", "lesson2"],
            "proven_strategies": ["strategy1", "strategy2"],
            "preventive_measures": ["measure1", "measure2"]
        }}
        """,
        agent=agent,
        expected_output="JSON object with historical correlation results"
    )


def create_root_cause_task(agent) -> Task:
    """Task for root cause analysis synthesis"""
    return Task(
        description="""
        Synthesize all previous analysis to determine the most likely root cause:
        
        Use the outputs from:
        - Alert triage analysis
        - Log analysis results
        - Metrics analysis results
        - Historical incident correlation
        
        Your task is to:
        1. Identify the most likely root cause
        2. Provide supporting evidence
        3. Assess confidence level
        4. Rule out alternative causes
        5. Explain the failure chain
        
        Output your analysis as a JSON object with the following structure:
        {{
            "root_cause": "primary root cause description",
            "supporting_evidence": ["evidence1", "evidence2"],
            "confidence_level": "High|Medium|Low",
            "alternative_causes": ["cause1", "cause2"],
            "failure_chain": "step-by-step explanation of how the failure occurred",
            "contributing_factors": ["factor1", "factor2"]
        }}
        """,
        agent=agent,
        expected_output="JSON object with root cause analysis"
    )


def create_action_recommendation_task(agent) -> Task:
    """Task for generating action recommendations"""
    return Task(
        description="""
        Based on the root cause analysis, provide specific action recommendations:
        
        Your task is to:
        1. Provide immediate mitigation steps
        2. Suggest long-term resolution actions
        3. Prioritize actions by impact and effort
        4. Include rollback procedures if applicable
        5. Recommend monitoring and validation steps
        
        Output your recommendations as a JSON object with the following structure:
        {{
            "immediate_actions": [
                {{"action": "description", "priority": "High|Medium|Low", "estimated_time": "duration"}}
            ],
            "long_term_actions": [
                {{"action": "description", "priority": "High|Medium|Low", "estimated_effort": "effort"}}
            ],
            "rollback_procedures": ["step1", "step2"],
            "monitoring_steps": ["monitor1", "monitor2"],
            "validation_criteria": ["criteria1", "criteria2"]
        }}
        """,
        agent=agent,
        expected_output="JSON object with action recommendations"
    )


def create_post_incident_task(agent) -> Task:
    """Task for generating post-incident report"""
    return Task(
        description="""
        Generate a comprehensive post-incident report based on all analysis:
        
        Your task is to:
        1. Create incident timeline
        2. Summarize impact and affected services
        3. Document root cause and resolution
        4. Identify lessons learned
        5. Recommend preventive measures
        
        Output your report as a JSON object with the following structure:
        {{
            "incident_summary": "brief summary of the incident",
            "timeline": [
                {{"time": "timestamp", "event": "description", "impact": "impact level"}}
            ],
            "impact_analysis": {{
                "services_affected": ["service1", "service2"],
                "users_impacted": "estimate",
                "business_impact": "description",
                "duration": "total incident duration"
            }},
            "resolution_summary": "how the incident was resolved",
            "lessons_learned": ["lesson1", "lesson2"],
            "preventive_measures": ["measure1", "measure2"],
            "action_items": [
                {{"action": "description", "owner": "team", "due_date": "date"}}
            ]
        }}
        """,
        agent=agent,
        expected_output="JSON object with comprehensive post-incident report"
    )