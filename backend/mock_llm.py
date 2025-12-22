"""
Mock LLM for demo purposes when Ollama is not available
Provides realistic responses for incident analysis
"""

import json
import random
from typing import Any, Dict, List, Optional


class MockOllamaLLM:
    """Mock LLM that simulates Ollama responses for demo purposes"""
    
    def __init__(self, model: str = "llama3", **kwargs):
        self.model = model
        self.kwargs = kwargs
    
    def invoke(self, prompt: str) -> str:
        """Generate mock response based on prompt content"""
        prompt_lower = prompt.lower()
        
        # Simple health check
        if prompt == "Hello":
            return "Hello! I'm a mock LLM ready to help with incident analysis."
        
        # Alert triage responses
        if "alert" in prompt_lower and "triage" in prompt_lower:
            return json.dumps({
                "severity": "P1",
                "business_impact": "High - User service degradation affecting 15% of users",
                "affected_services": ["user-service", "session-cache"],
                "escalation_needed": True,
                "estimated_users_affected": 1500,
                "priority_justification": "Memory exhaustion causing service instability"
            })
        
        # Log analysis responses
        if "log" in prompt_lower and "analysis" in prompt_lower:
            return json.dumps({
                "key_errors": [
                    "OutOfMemoryError: Java heap space",
                    "GC overhead limit exceeded",
                    "Unable to allocate memory for session cache"
                ],
                "error_patterns": [
                    "Memory allocation failures increasing since 10:25 AM",
                    "Session cache size growing exponentially",
                    "Garbage collection frequency doubled"
                ],
                "timeline": [
                    {"timestamp": "10:25:00", "severity": "WARN", "event": "Memory usage above 80%"},
                    {"timestamp": "10:28:30", "severity": "ERROR", "event": "First OutOfMemoryError"},
                    {"timestamp": "10:30:00", "severity": "CRITICAL", "event": "Service degradation begins"}
                ]
            })
        
        # Metrics analysis responses
        if "metrics" in prompt_lower and "analysis" in prompt_lower:
            return json.dumps({
                "threshold_breaches": [
                    {
                        "metric": "memory_usage_percent",
                        "value": "94.2%",
                        "threshold": "90%",
                        "severity": "Critical",
                        "duration": "5 minutes"
                    },
                    {
                        "metric": "heap_utilization",
                        "value": "98.1%",
                        "threshold": "85%",
                        "severity": "Critical",
                        "duration": "3 minutes"
                    }
                ],
                "resource_constraints": [
                    "Memory allocation rate exceeding deallocation by 15MB/min",
                    "Heap fragmentation at 23% (normal: <10%)",
                    "GC pause times increased 300% from baseline"
                ],
                "performance_impact": "Response times increased 250%, error rate at 2.1%"
            })
        
        # Knowledge base responses
        if "knowledge" in prompt_lower or "historical" in prompt_lower:
            return json.dumps({
                "similar_incidents": [
                    {
                        "incident_id": "INC-2024-0892",
                        "date": "2024-11-15",
                        "similarity_score": 0.87,
                        "root_cause": "Session cache memory leak in user authentication",
                        "resolution": "Implemented cache eviction policy and increased heap size"
                    },
                    {
                        "incident_id": "INC-2024-0654",
                        "date": "2024-10-03",
                        "similarity_score": 0.72,
                        "root_cause": "Memory leak in user session management",
                        "resolution": "Fixed session cleanup logic and added monitoring"
                    }
                ],
                "patterns": [
                    "Memory leaks typically occur after deployments with session management changes",
                    "User service memory issues often correlate with authentication load spikes",
                    "Previous incidents resolved within 2-4 hours with cache restart"
                ]
            })
        
        # Root cause analysis responses
        if "root cause" in prompt_lower:
            return json.dumps({
                "primary_cause": "Memory leak in user session caching mechanism causing heap exhaustion",
                "contributing_factors": [
                    "Recent deployment introduced session persistence bug",
                    "Cache eviction policy not properly configured",
                    "Increased user load during peak hours"
                ],
                "failure_chain": "Session creation → Cache storage without eviction → Memory accumulation → Heap exhaustion → OutOfMemoryError → Service degradation",
                "supporting_evidence": [
                    "Memory usage correlates with active session count",
                    "Error logs show session cache size growing continuously",
                    "Heap dump analysis reveals session objects not being garbage collected"
                ],
                "confidence_level": "High (85%)"
            })
        
        # Action recommendations responses
        if "recommendation" in prompt_lower or "action" in prompt_lower:
            return json.dumps({
                "immediate_actions": [
                    {
                        "action": "Restart user-service instances to clear memory",
                        "priority": "High",
                        "estimated_time": "5 minutes",
                        "risk": "Low - Rolling restart maintains availability"
                    },
                    {
                        "action": "Enable session cache eviction policy",
                        "priority": "High", 
                        "estimated_time": "10 minutes",
                        "risk": "Low - Configuration change only"
                    },
                    {
                        "action": "Increase heap size temporarily",
                        "priority": "Medium",
                        "estimated_time": "15 minutes",
                        "risk": "Medium - Requires service restart"
                    }
                ],
                "long_term_actions": [
                    {
                        "action": "Implement proper session lifecycle management",
                        "priority": "High",
                        "estimated_effort": "2-3 days",
                        "owner": "Backend Team"
                    },
                    {
                        "action": "Add memory usage alerting and monitoring",
                        "priority": "Medium",
                        "estimated_effort": "1 day",
                        "owner": "SRE Team"
                    },
                    {
                        "action": "Conduct load testing for session management",
                        "priority": "Medium",
                        "estimated_effort": "3-4 days",
                        "owner": "QA Team"
                    }
                ]
            })
        
        # Post-incident report responses
        if "post-incident" in prompt_lower or "report" in prompt_lower:
            return json.dumps({
                "incident_summary": "Memory leak in user session caching caused service degradation affecting 15% of users for 45 minutes",
                "timeline": [
                    "10:25 - Memory usage exceeded 80% threshold",
                    "10:28 - First OutOfMemoryError occurred",
                    "10:30 - Service degradation detected",
                    "10:35 - Incident declared and response team assembled",
                    "10:45 - Root cause identified as session cache leak",
                    "10:50 - Service restart initiated",
                    "11:15 - Service fully restored and monitoring confirmed"
                ],
                "lessons_learned": [
                    "Session cache monitoring was insufficient to detect gradual memory leaks",
                    "Deployment testing should include extended memory usage validation",
                    "Cache eviction policies need to be validated in staging environment",
                    "Automated alerting on memory trends would enable earlier detection"
                ],
                "preventive_measures": [
                    "Implement comprehensive memory monitoring with trend analysis",
                    "Add session cache size limits and eviction policies",
                    "Enhance deployment testing to include memory leak detection",
                    "Create runbooks for memory-related incident response",
                    "Schedule regular heap dump analysis for proactive monitoring"
                ],
                "action_items": [
                    "Deploy session management fix by EOD",
                    "Implement memory monitoring dashboard by end of week",
                    "Update deployment checklist to include memory validation",
                    "Schedule post-mortem review meeting with all stakeholders"
                ]
            })
        
        # Default response for unrecognized prompts
        return json.dumps({
            "analysis": "Mock LLM response for incident analysis",
            "confidence": "Medium",
            "recommendations": ["Review incident data", "Implement monitoring", "Follow up with team"]
        })


def get_mock_llm(**kwargs) -> MockOllamaLLM:
    """Get a mock LLM instance"""
    return MockOllamaLLM(**kwargs)