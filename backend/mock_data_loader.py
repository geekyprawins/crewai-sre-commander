"""
Mock Data Loader
Loads mock data for incident analysis
"""

import json
import os
from typing import List, Dict, Any


def load_json_file(filename: str) -> List[Dict[str, Any]]:
    """Load JSON data from mock_data directory"""
    try:
        file_path = os.path.join(os.path.dirname(__file__), 'mock_data', filename)
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return []


def load_alerts() -> List[Dict[str, Any]]:
    """Load mock alert data"""
    return load_json_file('alerts.json')


def load_logs() -> List[Dict[str, Any]]:
    """Load mock log data"""
    return load_json_file('logs.json')


def load_metrics() -> List[Dict[str, Any]]:
    """Load mock metrics data"""
    return load_json_file('metrics.json')


def load_past_incidents() -> List[Dict[str, Any]]:
    """Load mock historical incident data"""
    return load_json_file('past_incidents.json')


def get_sample_incident_data() -> Dict[str, Any]:
    """Get sample incident data for testing"""
    alerts = load_alerts()
    logs = load_logs()
    metrics = load_metrics()
    
    return {
        "alert": alerts[0] if alerts else "No alert data",
        "logs": logs[:3] if logs else "No log data",  # First 3 log entries
        "metrics": metrics[0] if metrics else "No metrics data"
    }