"""
Simplified Crew Implementation for Demo
Bypasses CrewAI complexity and directly uses mock LLM responses
"""

import json
import re
from datetime import datetime
from typing import Dict, Any
from llm_config import get_llm


def extract_json_from_text(text: str) -> Dict[str, Any]:
    """
    Extract JSON from text response, handling cases where LLM returns markdown or narrative text.
    Falls back to mock response if extraction fails.
    """
    try:
        # Try direct JSON parsing first
        return json.loads(text)
    except json.JSONDecodeError:
        # If not pure JSON, try to extract JSON from markdown code blocks
        json_match = re.search(r'```(?:json)?\n?(.*?)\n?```', text, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except json.JSONDecodeError:
                pass
        
        # If still no valid JSON, return a safe generic response
        from mock_llm import get_mock_llm
        mock_llm = get_mock_llm()
        # Use the mock LLM for this response
        return json.loads(mock_llm.invoke("analysis"))



class SimpleIncidentAnalysisCrew:
    """Simplified incident analysis crew using mock LLM"""
    
    def __init__(self):
        self.llm = get_llm()
    
    def analyze_incident(self, incident_data: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze incident using sequential agent workflow"""
        
        # Extract data from incident_data
        alert_data = incident_data.get("alert", "")
        log_data = incident_data.get("logs", "")
        metrics_data = incident_data.get("metrics", "")
        
        # Step 1: Alert Triage
        triage_prompt = f"""
        Analyze this alert for triage and severity assessment.
        Return ONLY a valid JSON object with no additional text.
        
        Alert Data: {alert_data}
        
        Provide triage analysis including severity, business impact, and affected services.
        """
        triage_response = self.llm.invoke(triage_prompt)
        try:
            triage_data = extract_json_from_text(triage_response)
        except Exception as e:
            raise ValueError(f"Failed to parse triage response: {triage_response}. Error: {str(e)}")
        
        # Step 2: Log Analysis
        log_prompt = f"""
        Analyze these logs for error patterns and timeline.
        Return ONLY a valid JSON object with no additional text.
        
        Log Data: {log_data}
        
        Provide log analysis including key errors, patterns, and timeline.
        """
        log_response = self.llm.invoke(log_prompt)
        try:
            log_data_parsed = extract_json_from_text(log_response)
        except Exception as e:
            raise ValueError(f"Failed to parse log analysis response: {log_response}. Error: {str(e)}")
        
        # Step 3: Metrics Analysis
        metrics_prompt = f"""
        Analyze these metrics for performance issues and thresholds.
        Return ONLY a valid JSON object with no additional text.
        
        Metrics Data: {metrics_data}
        
        Provide metrics analysis including threshold breaches and resource constraints.
        """
        metrics_response = self.llm.invoke(metrics_prompt)
        try:
            metrics_data_parsed = extract_json_from_text(metrics_response)
        except Exception as e:
            raise ValueError(f"Failed to parse metrics analysis response: {metrics_response}. Error: {str(e)}")
        
        # Step 4: Knowledge Base Correlation
        kb_prompt = f"""
        Search knowledge base for similar incidents based on data provided.
        Return ONLY a valid JSON object with no additional text.
        
        Alert: {alert_data}
        Logs: {log_data}
        Metrics: {metrics_data}
        
        Provide historical incident correlation and patterns.
        """
        kb_response = self.llm.invoke(kb_prompt)
        try:
            kb_data = extract_json_from_text(kb_response)
        except Exception as e:
            raise ValueError(f"Failed to parse knowledge base response: {kb_response}. Error: {str(e)}")
        
        # Step 5: Root Cause Analysis
        rca_prompt = f"""
        Determine root cause based on all available data.
        Return ONLY a valid JSON object with no additional text.
        
        Triage: {triage_response}
        Logs: {log_response}
        Metrics: {metrics_response}
        Knowledge: {kb_response}
        
        Provide comprehensive root cause analysis.
        """
        rca_response = self.llm.invoke(rca_prompt)
        try:
            rca_data = extract_json_from_text(rca_response)
        except Exception as e:
            raise ValueError(f"Failed to parse root cause analysis response: {rca_response}. Error: {str(e)}")
        
        # Step 6: Action Recommendations
        action_prompt = f"""
        Recommend immediate and long-term actions based on root cause analysis.
        Return ONLY a valid JSON object with no additional text.
        
        Root Cause: {rca_response}
        Severity: {triage_data.get('severity', 'Unknown')}
        
        Provide actionable recommendations with priorities and timelines.
        """
        action_response = self.llm.invoke(action_prompt)
        try:
            action_data = extract_json_from_text(action_response)
        except Exception as e:
            raise ValueError(f"Failed to parse action recommendations response: {action_response}. Error: {str(e)}")
        
        # Step 7: Post-Incident Report
        report_prompt = f"""
        Generate post-incident report based on complete analysis.
        Return ONLY a valid JSON object with no additional text.
        
        Incident Summary: {triage_response}
        Root Cause: {rca_response}
        Actions Taken: {action_response}
        
        Provide comprehensive post-incident report with lessons learned.
        """
        report_response = self.llm.invoke(report_prompt)
        try:
            report_data = extract_json_from_text(report_response)
        except Exception as e:
            raise ValueError(f"Failed to parse post-incident report response: {report_response}. Error: {str(e)}")
        
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