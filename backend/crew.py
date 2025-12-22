"""
CrewAI Crew Configuration for SRE Incident Commander
Orchestrates the multi-agent incident analysis workflow
"""

import json
from typing import Dict, Any
from crewai import Crew, Process

# Import agents
from agents.alert_triage_agent import create_alert_triage_agent
from agents.log_analysis_agent import create_log_analysis_agent
from agents.metrics_analysis_agent import create_metrics_analysis_agent
from agents.knowledge_base_agent import create_knowledge_base_agent
from agents.root_cause_agent import create_root_cause_agent
from agents.action_recommendation_agent import create_action_recommendation_agent
from agents.post_incident_agent import create_post_incident_agent

# Import tasks
from tasks.incident_tasks import (
    create_alert_triage_task,
    create_log_analysis_task,
    create_metrics_analysis_task,
    create_knowledge_base_task,
    create_root_cause_task,
    create_action_recommendation_task,
    create_post_incident_task
)

# Import mock data
from mock_data_loader import load_past_incidents


class IncidentAnalysisCrew:
    """Main crew for incident analysis"""
    
    def __init__(self):
        # Initialize agents
        self.alert_triage_agent = create_alert_triage_agent()
        self.log_analysis_agent = create_log_analysis_agent()
        self.metrics_analysis_agent = create_metrics_analysis_agent()
        self.knowledge_base_agent = create_knowledge_base_agent()
        self.root_cause_agent = create_root_cause_agent()
        self.action_recommendation_agent = create_action_recommendation_agent()
        self.post_incident_agent = create_post_incident_agent()
        
        # Load historical data
        self.past_incidents = load_past_incidents()
    
    def analyze_incident(self, incident_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run the complete incident analysis workflow
        
        Args:
            incident_data: Dictionary containing alert, logs, and metrics data
            
        Returns:
            Complete incident analysis results
        """
        
        # Create tasks with incident data
        tasks = [
            create_alert_triage_task(self.alert_triage_agent, incident_data),
            create_log_analysis_task(self.log_analysis_agent, incident_data),
            create_metrics_analysis_task(self.metrics_analysis_agent, incident_data),
            create_knowledge_base_task(self.knowledge_base_agent, self.past_incidents),
            create_root_cause_task(self.root_cause_agent),
            create_action_recommendation_task(self.action_recommendation_agent),
            create_post_incident_task(self.post_incident_agent)
        ]
        
        # Create crew with sequential process
        crew = Crew(
            agents=[
                self.alert_triage_agent,
                self.log_analysis_agent,
                self.metrics_analysis_agent,
                self.knowledge_base_agent,
                self.root_cause_agent,
                self.action_recommendation_agent,
                self.post_incident_agent
            ],
            tasks=tasks,
            process=Process.sequential,
            verbose=True
        )
        
        # Execute the crew workflow
        try:
            result = crew.kickoff()
            
            # Parse and structure the final result
            return self._structure_results(result, tasks)
            
        except Exception as e:
            return {
                "error": f"Incident analysis failed: {str(e)}",
                "status": "failed"
            }
    
    def _structure_results(self, crew_result: str, tasks: list) -> Dict[str, Any]:
        """
        Structure the crew results into a comprehensive incident report
        
        Args:
            crew_result: Raw result from crew execution
            tasks: List of executed tasks
            
        Returns:
            Structured incident analysis results
        """
        
        try:
            # Extract individual task results
            task_results = {}
            
            # In a real implementation, you would parse individual task outputs
            # For this demo, we'll create a structured response
            
            return {
                "status": "completed",
                "incident_id": f"INC-{hash(str(crew_result)) % 10000:04d}",
                "analysis_timestamp": "2024-12-22T10:35:00Z",
                "severity": "P1",
                "summary": {
                    "title": "Memory leak causing service degradation",
                    "affected_services": ["user-service", "api-gateway"],
                    "root_cause": "Memory leak in user session caching after deployment",
                    "confidence": "High"
                },
                "triage": {
                    "severity": "P1",
                    "urgency": "High",
                    "business_impact": "User authentication failures affecting 15% of requests",
                    "affected_services": ["user-service", "api-gateway"]
                },
                "analysis": {
                    "logs": {
                        "key_errors": ["OutOfMemoryError: Java heap space", "GC overhead limit exceeded"],
                        "error_patterns": ["Memory exhaustion", "Frequent garbage collection"],
                        "timeline": [
                            {"timestamp": "10:29:45Z", "event": "First OutOfMemoryError", "severity": "ERROR"},
                            {"timestamp": "10:30:12Z", "event": "GC overhead limit exceeded", "severity": "WARN"}
                        ]
                    },
                    "metrics": {
                        "resource_constraints": ["Memory usage at 94.2%", "Heap utilization critical"],
                        "threshold_breaches": [
                            {"metric": "memory_usage", "value": "94.2%", "threshold": "90%", "severity": "Critical"}
                        ]
                    },
                    "historical_correlation": {
                        "similar_incidents": [
                            {"id": "INC-2024-001", "similarity": "Memory leak after deployment", "outcome": "Rollback and hotfix"}
                        ],
                        "proven_strategies": ["Rollback to previous version", "Memory profiling", "Gradual deployment"]
                    }
                },
                "root_cause": {
                    "primary_cause": "Memory leak introduced in user session caching logic in v2.1.3 deployment",
                    "supporting_evidence": [
                        "Memory usage increased steadily after deployment",
                        "OutOfMemoryError exceptions in user-service",
                        "Similar pattern in INC-2024-001"
                    ],
                    "confidence_level": "High",
                    "failure_chain": "Deployment v2.1.3 → Session cache memory leak → Heap exhaustion → OutOfMemoryError → Service restarts → User impact"
                },
                "recommendations": {
                    "immediate_actions": [
                        {"action": "Rollback user-service to v2.1.2", "priority": "High", "estimated_time": "5 minutes"},
                        {"action": "Restart affected service instances", "priority": "High", "estimated_time": "2 minutes"},
                        {"action": "Monitor memory usage closely", "priority": "Medium", "estimated_time": "Ongoing"}
                    ],
                    "long_term_actions": [
                        {"action": "Fix memory leak in session caching", "priority": "High", "estimated_effort": "2-4 hours"},
                        {"action": "Implement memory profiling in staging", "priority": "Medium", "estimated_effort": "1 day"},
                        {"action": "Add heap dump collection on OOM", "priority": "Medium", "estimated_effort": "4 hours"}
                    ]
                },
                "post_incident_report": {
                    "incident_summary": "Memory leak in user-service v2.1.3 caused service degradation and authentication failures",
                    "impact_analysis": {
                        "services_affected": ["user-service", "api-gateway"],
                        "users_impacted": "~15% of active users",
                        "business_impact": "Authentication failures and increased response times",
                        "duration": "Ongoing (detected 5 minutes ago)"
                    },
                    "lessons_learned": [
                        "Need better memory testing in staging environment",
                        "Implement gradual rollout strategy for deployments",
                        "Add proactive memory monitoring alerts"
                    ],
                    "preventive_measures": [
                        "Memory profiling in CI/CD pipeline",
                        "Automated rollback triggers on memory thresholds",
                        "Enhanced staging environment testing"
                    ]
                },
                "raw_crew_output": str(crew_result)
            }
            
        except Exception as e:
            return {
                "error": f"Failed to structure results: {str(e)}",
                "status": "failed",
                "raw_output": str(crew_result)
            }