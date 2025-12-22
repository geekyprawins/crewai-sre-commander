import React, { useState } from 'react'

const IncidentForm = ({ onSubmit }) => {
  const [formData, setFormData] = useState({
    alert: '',
    logs: '',
    metrics: ''
  })

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    onSubmit(formData)
  }

  const loadSampleData = () => {
    setFormData({
      alert: `{
  "id": "alert-001",
  "timestamp": "2024-12-22T10:30:00Z",
  "severity": "critical",
  "service": "user-service",
  "message": "Memory usage exceeded 90% threshold",
  "metrics": {
    "memory_usage_percent": 94.2,
    "cpu_usage_percent": 78.5
  }
}`,
      logs: `[
  {
    "timestamp": "2024-12-22T10:29:45Z",
    "level": "ERROR",
    "service": "user-service",
    "message": "OutOfMemoryError: Java heap space",
    "stack_trace": "java.lang.OutOfMemoryError: Java heap space\\n\\tat com.example.UserService.processRequest(UserService.java:142)"
  },
  {
    "timestamp": "2024-12-22T10:30:12Z",
    "level": "WARN",
    "service": "user-service",
    "message": "GC overhead limit exceeded"
  }
]`,
      metrics: `{
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
}`
    })
  }

  return (
    <div className="bg-white rounded-lg shadow-sm border p-6">
      <div className="flex justify-between items-center mb-6">
        <h2 className="text-xl font-semibold text-gray-900">Incident Analysis</h2>
        <button
          type="button"
          onClick={loadSampleData}
          className="text-sm bg-gray-100 text-gray-700 px-3 py-1 rounded-md hover:bg-gray-200 transition-colors"
        >
          Load Sample Data
        </button>
      </div>

      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label htmlFor="alert" className="block text-sm font-medium text-gray-700 mb-2">
            Alert Data
          </label>
          <textarea
            id="alert"
            name="alert"
            rows={6}
            value={formData.alert}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-sre-blue focus:border-transparent"
            placeholder="Paste alert JSON data here..."
            required
          />
        </div>

        <div>
          <label htmlFor="logs" className="block text-sm font-medium text-gray-700 mb-2">
            Log Data
          </label>
          <textarea
            id="logs"
            name="logs"
            rows={6}
            value={formData.logs}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-sre-blue focus:border-transparent"
            placeholder="Paste log data here..."
            required
          />
        </div>

        <div>
          <label htmlFor="metrics" className="block text-sm font-medium text-gray-700 mb-2">
            Metrics Data
          </label>
          <textarea
            id="metrics"
            name="metrics"
            rows={6}
            value={formData.metrics}
            onChange={handleChange}
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-sre-blue focus:border-transparent"
            placeholder="Paste metrics JSON data here..."
            required
          />
        </div>

        <button
          type="submit"
          className="w-full bg-sre-blue text-white px-4 py-3 rounded-md hover:bg-blue-700 transition-colors font-medium"
        >
          Analyze Incident
        </button>
      </form>
    </div>
  )
}

export default IncidentForm