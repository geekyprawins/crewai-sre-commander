# SRE Incident Commander

An AI-powered incident analysis and response system that uses CrewAI multi-agent workflows with Ollama to provide comprehensive incident analysis, root cause determination, and actionable recommendations.

## 🎯 Project Overview

The SRE Incident Commander simulates an expert SRE team working together to analyze incidents. It takes in alerts, logs, and metrics data, then runs a sophisticated multi-agent analysis to provide:

- **Incident Severity Assessment** - Automated triage and priority classification
- **Root Cause Analysis** - Deep analysis using logs, metrics, and historical patterns
- **Actionable Recommendations** - Immediate mitigation steps and long-term fixes
- **Post-Incident Reports** - Comprehensive documentation and lessons learned

## 🏗️ Architecture

### Multi-Agent CrewAI Workflow

The system employs 7 specialized AI agents that work sequentially:

1. **Alert Triage Agent** - Assesses severity and business impact
2. **Log Analysis Agent** - Parses error patterns and anomalies
3. **Metrics Analysis Agent** - Identifies performance bottlenecks
4. **Knowledge Base Agent** - Correlates with historical incidents
5. **Root Cause Analysis Agent** - Synthesizes findings to determine primary cause
6. **Action Recommendation Agent** - Provides specific mitigation steps
7. **Post-Incident Report Agent** - Generates comprehensive documentation

### Technology Stack

- **Backend**: Python 3.11 + FastAPI
- **AI Framework**: CrewAI for multi-agent orchestration
- **LLM**: Ollama (local) with llama3 model
- **Frontend**: React + Vite + Tailwind CSS
- **Data**: JSON mock files (no external dependencies)

### How Ollama is Used

- **Local LLM Execution**: All AI processing runs locally via Ollama HTTP API
- **Model Configuration**: Centralized in `llm_config.py` with explicit Ollama settings
- **No Cloud Dependencies**: Zero reliance on OpenAI, Anthropic, or other cloud LLMs
- **Deterministic Analysis**: Low temperature settings for consistent results

## 🚀 Setup Instructions

### Prerequisites

1. **Install Ollama**
   ```bash
   # macOS
   brew install ollama
   
   # Linux
   curl -fsSL https://ollama.ai/install.sh | sh
   
   # Windows - Download from https://ollama.ai/download
   ```

2. **Pull the LLM Model**
   ```bash
   ollama pull llama3
   # Alternative models: mistral, orca-mini
   ```

3. **Start Ollama Service**
   ```bash
   ollama serve
   # Runs on http://localhost:11434
   ```

### Backend Setup

1. **Navigate to Backend Directory**
   ```bash
   cd sre-incident-commander/backend
   ```

2. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the FastAPI Server**
   ```bash
   python main.py
   # Runs on http://localhost:12000
   ```

### Frontend Setup

1. **Navigate to Frontend Directory**
   ```bash
   cd sre-incident-commander/frontend
   ```

2. **Install Node Dependencies**
   ```bash
   npm install
   ```

3. **Start the Development Server**
   ```bash
   npm run dev
   # Runs on http://localhost:12001
   ```

## 🎮 Demo Walkthrough

### Quick Demo with Sample Data

1. **Access the Application**
   - Open http://localhost:12001 in your browser
   - You'll see the SRE Incident Commander dashboard

2. **Run Sample Analysis**
   - Click "Analyze Sample Incident" button
   - This demonstrates a memory leak scenario with realistic data
   - Watch the loading screen show each agent's progress

3. **Review Results**
   - **Severity Badge**: Shows P1-High priority
   - **Executive Summary**: Affected services and business impact
   - **Root Cause**: Memory leak in user session caching
   - **Evidence**: Supporting logs and metrics analysis
   - **Recommendations**: Immediate and long-term actions
   - **Post-Incident Report**: Lessons learned and preventive measures

### Custom Incident Analysis

1. **Load Sample Data**
   - Click "Load Sample Data" in the incident form
   - Modify the JSON data as needed

2. **Submit for Analysis**
   - Click "Analyze Incident"
   - The 7-agent workflow will process your data
   - Results appear in structured format

### Sample Incident Payload

```json
{
  "alert": {
    "id": "alert-001",
    "timestamp": "2024-12-22T10:30:00Z",
    "severity": "critical",
    "service": "user-service",
    "message": "Memory usage exceeded 90% threshold",
    "metrics": {
      "memory_usage_percent": 94.2,
      "cpu_usage_percent": 78.5
    }
  },
  "logs": [
    {
      "timestamp": "2024-12-22T10:29:45Z",
      "level": "ERROR",
      "service": "user-service",
      "message": "OutOfMemoryError: Java heap space",
      "stack_trace": "java.lang.OutOfMemoryError: Java heap space\\n\\tat com.example.UserService.processRequest(UserService.java:142)"
    }
  ],
  "metrics": {
    "timestamp": "2024-12-22T10:30:00Z",
    "service": "user-service",
    "metrics": {
      "memory_usage_bytes": 2030043136,
      "memory_limit_bytes": 2147483648,
      "cpu_usage_percent": 78.5,
      "heap_used_mb": 1890,
      "heap_max_mb": 2048,
      "requests_per_second": 850,
      "error_rate_percent": 2.1
    }
  }
}
```

## 📁 Project Structure

```
sre-incident-commander/
├── backend/
│   ├── agents/                    # CrewAI agent definitions
│   │   ├── alert_triage_agent.py
│   │   ├── log_analysis_agent.py
│   │   ├── metrics_analysis_agent.py
│   │   ├── knowledge_base_agent.py
│   │   ├── root_cause_agent.py
│   │   ├── action_recommendation_agent.py
│   │   └── post_incident_agent.py
│   ├── tasks/                     # CrewAI task definitions
│   │   └── incident_tasks.py
│   ├── mock_data/                 # Realistic test data
│   │   ├── alerts.json
│   │   ├── logs.json
│   │   ├── metrics.json
│   │   └── past_incidents.json
│   ├── llm_config.py             # Ollama configuration
│   ├── crew.py                   # Main CrewAI orchestration
│   ├── main.py                   # FastAPI application
│   ├── mock_data_loader.py       # Data loading utilities
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/           # React components
│   │   │   ├── Header.jsx
│   │   │   ├── IncidentForm.jsx
│   │   │   ├── IncidentResults.jsx
│   │   │   ├── LoadingSpinner.jsx
│   │   │   └── SeverityBadge.jsx
│   │   ├── App.jsx              # Main application
│   │   ├── main.jsx             # React entry point
│   │   └── index.css            # Tailwind styles
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
└── README.md
```

## 🔧 API Endpoints

### Health Check
```bash
GET /health
# Returns API and LLM status
```

### Analyze Incident
```bash
POST /analyze-incident
Content-Type: application/json

{
  "alert": "alert data string",
  "logs": "log data string", 
  "metrics": "metrics data string"
}
```

### Sample Incident
```bash
GET /sample-incident
# Returns sample incident data

POST /analyze-sample
# Analyzes pre-loaded sample incident
```

## 🎯 Resume-Ready Bullet Points

- **Built full-stack AI incident response system** using CrewAI multi-agent framework with 7 specialized agents for comprehensive incident analysis
- **Implemented local LLM integration** with Ollama, eliminating cloud dependencies and ensuring data privacy for enterprise SRE workflows
- **Designed sequential agent pipeline** that processes alerts, logs, and metrics to deliver root cause analysis and actionable recommendations
- **Created production-ready FastAPI backend** with structured JSON APIs and comprehensive error handling for incident data processing
- **Developed responsive React frontend** with Tailwind CSS, featuring real-time analysis progress tracking and structured incident reporting
- **Engineered realistic mock data scenarios** including memory leaks and database exhaustion for comprehensive system testing and demos
- **Implemented enterprise-grade incident management** with severity classification, evidence correlation, and post-incident documentation

## 🔍 Key Features

### AI-Powered Analysis
- **Multi-Agent Collaboration**: 7 specialized agents work together
- **Pattern Recognition**: Correlates current incidents with historical data
- **Evidence-Based Conclusions**: Provides supporting evidence for all findings

### Production-Ready Design
- **Structured JSON APIs**: Clean, documented endpoints
- **Error Handling**: Comprehensive error management and user feedback
- **Scalable Architecture**: Modular design for easy extension

### Enterprise Features
- **Severity Classification**: P0-P3 priority system
- **Timeline Reconstruction**: Chronological incident progression
- **Action Prioritization**: Immediate vs. long-term recommendations
- **Lessons Learned**: Automated post-incident documentation

## 🚨 Troubleshooting

### Common Issues

1. **Ollama Connection Failed**
   ```bash
   # Check if Ollama is running
   curl http://localhost:11434/api/version
   
   # Restart Ollama if needed
   ollama serve
   ```

2. **Model Not Found**
   ```bash
   # Pull the required model
   ollama pull llama3
   ```

3. **Backend Import Errors**
   ```bash
   # Install missing dependencies
   pip install -r requirements.txt
   ```

4. **Frontend Build Issues**
   ```bash
   # Clear node modules and reinstall
   rm -rf node_modules package-lock.json
   npm install
   ```

## 🔮 Future Enhancements

- **Real-time Monitoring Integration**: Connect to Prometheus, Grafana
- **Slack/Teams Integration**: Automated incident notifications
- **Custom Agent Training**: Fine-tune agents for specific environments
- **Historical Incident Database**: Persistent storage for pattern learning
- **Multi-Model Support**: Support for different Ollama models
- **Advanced Visualizations**: Interactive timeline and dependency graphs

---

**Built with ❤️ by Praveen Varma for SRE teams who want AI-powered incident response without cloud dependencies.**