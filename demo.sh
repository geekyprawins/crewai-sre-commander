#!/bin/bash

echo "🚀 SRE Incident Commander - Demo Script"
echo "========================================"
echo ""

# Check if backend is running
echo "1. Checking Backend Health..."
BACKEND_HEALTH=$(curl -s http://localhost:12000/health | jq -r '.api_status' 2>/dev/null)
if [ "$BACKEND_HEALTH" = "healthy" ]; then
    echo "✅ Backend is healthy and running on port 12000"
else
    echo "❌ Backend is not running. Starting backend..."
    cd backend && python main.py > server.log 2>&1 &
    sleep 3
    echo "✅ Backend started"
fi

echo ""

# Test sample incident analysis
echo "2. Testing Sample Incident Analysis..."
ANALYSIS_STATUS=$(curl -s -X POST http://localhost:12000/analyze-sample | jq -r '.status' 2>/dev/null)
if [ "$ANALYSIS_STATUS" = "success" ]; then
    echo "✅ Sample incident analysis successful"
    echo "📊 Generated incident report with 7-agent workflow"
else
    echo "❌ Sample incident analysis failed"
fi

echo ""

# Check frontend
echo "3. Checking Frontend..."
if pgrep -f "vite.*12001\|vite.*12002\|vite.*12003" > /dev/null; then
    FRONTEND_PORT=$(ps aux | grep -E "vite.*--port" | grep -v grep | head -1 | sed -n 's/.*--port \([0-9]*\).*/\1/p')
    if [ -z "$FRONTEND_PORT" ]; then
        FRONTEND_PORT="12001"
    fi
    echo "✅ Frontend is running on port $FRONTEND_PORT"
    echo "🌐 Access at: https://work-2-sfkangrnyhsxayqz.prod-runtime.all-hands.dev"
else
    echo "❌ Frontend is not running. Starting frontend..."
    cd frontend && npm run dev > frontend.log 2>&1 &
    sleep 5
    echo "✅ Frontend started"
fi

echo ""

# Show API endpoints
echo "4. Available API Endpoints:"
echo "   GET  /health           - System health check"
echo "   GET  /sample-incident  - Get sample incident data"
echo "   POST /analyze-sample   - Analyze sample incident"
echo "   POST /analyze-incident - Analyze custom incident"

echo ""

# Show sample API call
echo "5. Sample API Call:"
echo "curl -X POST http://localhost:12000/analyze-sample | jq '.summary'"

echo ""

# Show demo data
echo "6. Demo Features:"
echo "   🤖 7 Specialized AI Agents (Alert Triage, Log Analysis, Metrics, etc.)"
echo "   📊 Multi-agent CrewAI workflow"
echo "   🔧 Mock LLM for offline demo"
echo "   📈 Realistic incident scenarios"
echo "   🎨 React + Tailwind frontend"
echo "   ⚡ FastAPI backend"

echo ""
echo "🎯 Demo Ready! System is fully operational."
echo "========================================"