"""
Simplified Crew Implementation for Demo
Bypasses CrewAI complexity and directly uses mock LLM responses
"""

import json
from datetime import datetime
from typing import Dict, Any
from mock_llm import get_mock_llm


class SimpleIncidentAnalysisCrew:
    """Simplified incident analysis crew using mock LLM"""
    
    def __init__(self):
        self.llm = get_mock_llm()
    
    def analyze_incident(self, incident_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze incident using sequential agent workflow"""
        
        # Extract data from incident_data
        alert_data = incident_data.get("alert", "")
        log_data = incident_data.get("logs", "")
        metrics_data = incident_data.get("metrics", "")
        
        # Step 1: Alert Triage
        triage_prompt = f"""
        Analyze this alert for triage and severity assessment:
        Alert Data: {alert_data}
        
        Provide triage analysis including severity, business impact, and affected services.
        """
        triage_response = self.llm.invoke(triage_prompt)
        triage_data = json.loads(triage_response)
        
        # Step 2: Log Analysis
        log_prompt = f"""
        Analyze these logs for error patterns and timeline:
        Log Data: {log_data}
        
        Provide log analysis including key errors, patterns, and timeline.
        """
        log_response = self.llm.invoke(log_prompt)
        log_data_parsed = json.loads(log_response)
        
        # Step 3: Metrics Analysis
        metrics_prompt = f"""
        Analyze these metrics for performance issues and thresholds:
        Metrics Data: {metrics_data}
        
        Provide metrics analysis including threshold breaches and resource constraints.
        """
        metrics_response = self.llm.invoke(metrics_prompt)
        metrics_data_parsed = json.loads(metrics_response)
        
        # Step 4: Knowledge Base Correlation
        kb_prompt = f"""
        Search knowledge base for similar incidents based on:
        Alert: {alert_data}
        Logs: {log_data}
        Metrics: {metrics_data}
        
        Provide historical incident correlation and patterns.
        """
        kb_response = self.llm.invoke(kb_prompt)
        kb_data = json.loads(kb_response)
        
        # Step 5: Root Cause Analysis
        rca_prompt = f"""
        Determine root cause based on all available data:
        Triage: {triage_response}
        Logs: {log_response}
        Metrics: {metrics_response}
        Knowledge: {kb_response}
        
        Provide comprehensive root cause analysis.
        """
        rca_response = self.llm.invoke(rca_prompt)
        rca_data = json.loads(rca_response)
        
        # Step 6: Action Recommendations
        action_prompt = f"""
        Recommend immediate and long-term actions based on:
        Root Cause: {rca_response}
        Severity: {triage_data.get('severity', 'Unknown')}
        
        Provide actionable recommendations with priorities and timelines.
        """
        action_response = self.llm.invoke(action_prompt)
        action_data = json.loads(action_response)
        
        # Step 7: Post-Incident Report
        report_prompt = f"""
        Generate post-incident report based on complete analysis:
        Incident Summary: {triage_response}
        Root Cause: {rca_response}
        Actions Taken: {action_response}
        
        Provide comprehensive post-incident report with lessons learned.
        """
        report_response = self.llm.invoke(report_prompt)
        report_data = json.loads(report_response)
        
        # Combine all results
        return {
            "incident_id": f"INC-{datetime.now().strftime('%Y%m%d-%H%M%S')}",
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "title": f"Memory leak causing service degradation - {triage_data.get('severity', 'P1')}",
                "severity": triage_data.get("severity", "P1"),
                "affected_services": triage_data.get("affected_services", ["user-service"]),
                "root_cause": rca_data.get("primary_cause", "Memory leak in session management")
            },
            "triage": triage_data,
            "analysis": {
                "logs": log_data_parsed,
                "metrics": metrics_data_parsed,
                "knowledge_base": kb_data
            },
            "root_cause": rca_data,
            "recommendations": action_data,
            "post_incident_report": report_data
        }