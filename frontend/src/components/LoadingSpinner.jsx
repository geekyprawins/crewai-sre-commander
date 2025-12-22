import React from 'react'

const LoadingSpinner = () => {
  return (
    <div className="bg-white rounded-lg shadow-sm border p-8">
      <div className="flex flex-col items-center justify-center space-y-4">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-sre-blue"></div>
        <div className="text-center">
          <h3 className="text-lg font-medium text-gray-900 mb-2">Analyzing Incident</h3>
          <p className="text-gray-600 mb-4">
            Our AI agents are working together to analyze your incident data...
          </p>
          <div className="space-y-2 text-sm text-gray-500">
            <div className="flex items-center justify-center space-x-2">
              <div className="w-2 h-2 bg-sre-blue rounded-full animate-pulse"></div>
              <span>Alert Triage Agent - Assessing severity</span>
            </div>
            <div className="flex items-center justify-center space-x-2">
              <div className="w-2 h-2 bg-sre-blue rounded-full animate-pulse animation-delay-200"></div>
              <span>Log Analysis Agent - Parsing error patterns</span>
            </div>
            <div className="flex items-center justify-center space-x-2">
              <div className="w-2 h-2 bg-sre-blue rounded-full animate-pulse animation-delay-400"></div>
              <span>Metrics Agent - Analyzing performance data</span>
            </div>
            <div className="flex items-center justify-center space-x-2">
              <div className="w-2 h-2 bg-sre-blue rounded-full animate-pulse animation-delay-600"></div>
              <span>Knowledge Base Agent - Correlating with history</span>
            </div>
            <div className="flex items-center justify-center space-x-2">
              <div className="w-2 h-2 bg-sre-blue rounded-full animate-pulse animation-delay-800"></div>
              <span>Root Cause Agent - Determining primary cause</span>
            </div>
            <div className="flex items-center justify-center space-x-2">
              <div className="w-2 h-2 bg-sre-blue rounded-full animate-pulse animation-delay-1000"></div>
              <span>Action Agent - Recommending solutions</span>
            </div>
            <div className="flex items-center justify-center space-x-2">
              <div className="w-2 h-2 bg-sre-blue rounded-full animate-pulse animation-delay-1200"></div>
              <span>Report Agent - Generating final report</span>
            </div>
          </div>
          <p className="text-xs text-gray-400 mt-4">
            This may take 30-60 seconds depending on Ollama model performance
          </p>
        </div>
      </div>
    </div>
  )
}

export default LoadingSpinner