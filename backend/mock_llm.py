"""
Mock LLM for demo purposes when Ollama is not available
Provides realistic responses for incident analysis
"""

import json
import random
from typing import Any, Dict, List, Optional, Iterator


class MockOllamaLLM:
    """Mock LLM that simulates Ollama responses for demo purposes"""
    
    def __init__(self, model: str = "llama3", **kwargs):
        self.model = model
        self.temperature = kwargs.get("temperature", 0.2)
        self.timeout = kwargs.get("timeout", 120)
        self.base_url = kwargs.get("base_url", "mock://localhost")
        self.kwargs = kwargs
    
    def invoke(self, prompt: str) -> str:
        """Generate mock response based on prompt content"""
        prompt_lower = prompt.lower()
        
        # Simple health check
        if prompt == "Hello":
            return "Hello! I'm a mock LLM ready to help with incident analysis."
        
        # Alert triage responses
        if ("alert" in prompt_lower and "triage" in prompt_lower) or ("alert" in prompt_lower and "severity" in prompt_lower):
            return json.dumps({
                "severity": "P1",
                "business_impact": "High - Service degradation with significant user impact",
                "affected_services": ["checkout-service", "payment-service"],
                "escalation_needed": True,
                "estimated_users_affected": 5000,
                "priority_justification": "Circuit breaker opened on payment service causing cascading failures"
            })
        
        # Log analysis responses
        if ("log" in prompt_lower and "analysis" in prompt_lower) or ("log" in prompt_lower and "error" in prompt_lower):
            return json.dumps({
                "key_errors": [
                    "503 Service Unavailable: PaymentService connection failed",
                    "Circuit breaker opened for PaymentService",
                    "Fallback response triggered for payment operations"
                ],
                "error_patterns": [
                    "Payment service failures increasing since 18:45",
                    "Checkout service error rate correlating with PaymentService availability",
                    "Circuit breaker state changes detected"
                ],
                "timeline": [
                    {"timestamp": "18:45:02", "severity": "ERROR", "event": "PaymentService 503 error"},
                    {"timestamp": "18:45:05", "severity": "WARN", "event": "Circuit breaker opened"},
                    {"timestamp": "18:45:10", "severity": "ERROR", "event": "Fallback response triggered"}
                ]
            })
        
        # Metrics analysis responses
        if ("metrics" in prompt_lower and "analysis" in prompt_lower) or ("metrics" in prompt_lower and "threshold" in prompt_lower):
            return json.dumps({
                "threshold_breaches": [
                    {
                        "metric": "payment_service_availability",
                        "value": "92%",
                        "threshold": "99.9%",
                        "severity": "Critical",
                        "duration": "2 minutes"
                    },
                    {
                        "metric": "checkout_error_rate",
                        "value": "8%",
                        "threshold": "1%",
                        "severity": "Critical",
                        "duration": "ongoing"
                    }
                ],
                "resource_constraints": [
                    "Payment service unavailable due to downstream failures",
                    "Circuit breaker limiting request flow to payment service",
                    "Latency increased 420% from baseline (p95: 4.2s)"
                ],
                "performance_impact": "Error rate at 8%, latency increased 4x, user impact significant"
            })
        
        # Knowledge base responses
        if ("knowledge" in prompt_lower or "historical" in prompt_lower or "similar" in prompt_lower):
            return json.dumps({
                "similar_incidents": [
                    {
                        "incident_id": "INC-2024-1203",
                        "date": "2024-12-01",
                        "similarity_score": 0.92,
                        "root_cause": "Downstream service degradation causing circuit breaker activation",
                        "resolution": "Restored downstream service, circuit breaker auto-recovery"
                    },
                    {
                        "incident_id": "INC-2024-0945",
                        "date": "2024-11-10",
                        "similarity_score": 0.81,
                        "root_cause": "Payment service timeout causing cascading failures",
                        "resolution": "Increased timeout values and improved fallback handling"
                    }
                ],
                "patterns": [
                    "Downstream service failures often trigger circuit breaker patterns",
                    "Payment service issues cascade to checkout service",
                    "Previous incidents resolved within 5-10 minutes with service restoration"
                ]
            })
        
        # Root cause analysis responses
        if "root cause" in prompt_lower or "determine" in prompt_lower:
            return json.dumps({
                "primary_cause": "PaymentService degradation causing cascading failures in CheckoutService",
                "contributing_factors": [
                    "Payment service unable to process requests (503 errors)",
                    "CheckoutService circuit breaker correctly opened to protect from cascading failures",
                    "No fallback mechanism for checkout operations"
                ],
                "failure_chain": "PaymentService unavailability → CheckoutService calls fail → Circuit breaker opens → Checkout operations fail → User-visible errors",
                "supporting_evidence": [
                    "Error logs show 503 errors from PaymentService",
                    "Circuit breaker state changed from closed to open at 18:45:05",
                    "Latency spike correlates with PaymentService failures",
                    "Metrics show payment_service_availability dropped to 92%"
                ],
                "confidence_level": "Very High (95%)"
            })
        
        # Action recommendations responses
        if ("recommendation" in prompt_lower or "action" in prompt_lower) and ("immediate" in prompt_lower or "based on" in prompt_lower):
            return json.dumps({
                "immediate_actions": [
                    {
                        "action": "Investigate PaymentService availability and restore if degraded",
                        "priority": "Critical",
                        "estimated_time": "5 minutes",
                        "risk": "Low - investigating existing issue"
                    },
                    {
                        "action": "Monitor circuit breaker state for auto-recovery",
                        "priority": "High",
                        "estimated_time": "1 minute",
                        "risk": "Low - monitoring only"
                    },
                    {
                        "action": "Implement checkout service fallback or queue mechanism",
                        "priority": "High",
                        "estimated_time": "10 minutes",
                        "risk": "Medium - requires code deployment"
                    }
                ],
                "long_term_actions": [
                    {
                        "action": "Implement graceful degradation for payment service failures",
                        "priority": "High",
                        "estimated_effort": "1-2 days",
                        "owner": "Backend Team"
                    },
                    {
                        "action": "Add comprehensive circuit breaker monitoring and alerting",
                        "priority": "High",
                        "estimated_effort": "1 day",
                        "owner": "SRE Team"
                    },
                    {
                        "action": "Improve dependency health monitoring and runbooks",
                        "priority": "Medium",
                        "estimated_effort": "2 days",
                        "owner": "SRE Team"
                    }
                ]
            })
        
        # Post-incident report responses
        if ("post-incident" in prompt_lower or "report" in prompt_lower) and ("based on" in prompt_lower or "analysis" in prompt_lower):
            return json.dumps({
                "incident_summary": "PaymentService degradation caused cascading CheckoutService failures affecting 5000+ users for 2 minutes",
                "timeline": [
                    "18:45:02 - PaymentService returned 503 Service Unavailable",
                    "18:45:05 - CheckoutService circuit breaker opened",
                    "18:45:10 - User-facing checkout errors began",
                    "18:45:15 - Incident alert triggered",
                    "18:46:30 - PaymentService restored",
                    "18:47:00 - Circuit breaker auto-recovered",
                    "18:47:30 - All services returned to normal"
                ],
                "lessons_learned": [
                    "Circuit breaker implementation correctly prevented cascading failures",
                    "Need better visibility into downstream service health",
                    "Fallback mechanisms needed for payment operations",
                    "Alert on circuit breaker state changes would enable faster response"
                ],
                "preventive_measures": [
                    "Implement service health probes for PaymentService",
                    "Add graceful degradation with fallback mechanisms",
                    "Improve monitoring of circuit breaker metrics",
                    "Create runbooks for common circuit breaker scenarios",
                    "Implement request queuing for payment operations"
                ],
                "action_items": [
                    "Deploy circuit breaker monitoring dashboard by EOD",
                    "Create PaymentService health probe within 24 hours",
                    "Design graceful degradation strategy within 1 week",
                    "Schedule post-mortem review with engineering team"
                ]
            })
        
        # Generic analysis fallback for unmatched prompts
        return json.dumps({
            "analysis": "Service dependency issue detected with cascading failure pattern",
            "severity": "P1",
            "affected_services": ["checkout-service", "payment-service"],
            "confidence": "High",
            "recommendations": [
                "Investigate downstream service health",
                "Verify circuit breaker and fallback mechanisms",
                "Review recent deployment changes",
                "Follow up with platform/infrastructure team"
            ]
        })
    
    def stream(self, prompt: str) -> Iterator[str]:
        """Stream response chunks (for streaming support)"""
        response = self.invoke(prompt)
        # Simulate streaming by yielding chunks
        chunk_size = 50
        for i in range(0, len(response), chunk_size):
            yield response[i:i + chunk_size]
    
    def call(self, prompt: str, **kwargs) -> str:
        """Call the LLM (alias for invoke)"""
        return self.invoke(prompt)
    
    def generate(self, prompts: List[str], **kwargs) -> Dict[str, Any]:
        """Generate responses for multiple prompts"""
        return {
            "generations": [[{"text": self.invoke(prompt), "finish_reason": "stop"}] for prompt in prompts]
        }
    
    def predict(self, text: str, **kwargs) -> str:
        """Predict/invoke with text input"""
        return self.invoke(text)
    
    @property
    def llm_type(self) -> str:
        """Return the type of LLM"""
        return "mock_ollama"
    
    def __call__(self, prompt: str, **kwargs) -> str:
        """Make the instance callable"""
        return self.invoke(prompt)


def get_mock_llm(**kwargs) -> MockOllamaLLM:
    """Get a mock LLM instance"""
    return MockOllamaLLM(**kwargs)


# Alias for backward compatibility with fallback in get_llm()
__all__ = ['MockOllamaLLM', 'get_mock_llm']
