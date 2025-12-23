#!/usr/bin/env python
"""Quick test script to verify the incident analysis crew works"""

import json
import sys

try:
    from simple_crew import SimpleIncidentAnalysisCrew
    from mock_llm import MockOllamaLLM
    
    print("✓ All imports successful")
    
    # Test 1: Create an LLM instance
    llm = MockOllamaLLM()
    print("✓ MockOllamaLLM instance created")
    
    # Test 2: Test basic invoke
    response = llm.invoke("alert triage severity")
    parsed = json.loads(response)
    print(f"✓ LLM invoke works, parsed response keys: {list(parsed.keys())}")
    
    # Test 3: Create crew and test with sample data
    crew = SimpleIncidentAnalysisCrew()
    print("✓ SimpleIncidentAnalysisCrew instance created")
    
    # Test 4: Run analysis with the provided data
    incident_data = {
        "alert": "CheckoutService error rate above threshold. Cascading failures detected across dependent services.",
        "logs": "2025-01-14 18:45:02 ERROR CheckoutService - Failed to call PaymentService (503 Service Unavailable)\n2025-01-14 18:45:05 WARN CheckoutService - Circuit breaker opened for PaymentService\n2025-01-14 18:45:10 ERROR CheckoutService - Fallback response triggered",
        "metrics": "payment_service_availability: dropped from 99.9% to 92%\ncheckout_error_rate: increased to 8%\nlatency_p95: increased to 4.2s\ncircuit_breaker_state: open"
    }
    
    result = crew.analyze_incident(incident_data)
    print("✓ analyze_incident completed successfully")
    
    # Test 5: Verify result structure
    assert "incident_id" in result
    assert "timestamp" in result
    assert "summary" in result
    assert "triage" in result
    print("✓ Result has expected structure")
    
    # Print sample of result
    print("\nSample Result:")
    print(json.dumps({
        "incident_id": result["incident_id"],
        "summary": result["summary"],
        "triage": result["triage"]
    }, indent=2))
    
    print("\n✓ All tests passed!")
    sys.exit(0)
    
except Exception as e:
    print(f"✗ Error: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
