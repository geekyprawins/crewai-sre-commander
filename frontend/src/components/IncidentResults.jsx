import React from 'react'
import SeverityBadge from './SeverityBadge'

// Helper function to ensure value is an array
const ensureArray = (value) => {
  if (!value) return []
  if (Array.isArray(value)) return value
  if (typeof value === 'string') {
    // Try to parse as JSON if it's a string
    try {
      const parsed = JSON.parse(value)
      return Array.isArray(parsed) ? parsed : [value]
    } catch {
      return [value]
    }
  }
  return [value]
}

// Helper function to safely render any value
const renderValue = (value) => {
  if (value === null || value === undefined) return 'N/A'
  if (typeof value === 'string') return value
  if (typeof value === 'number' || typeof value === 'boolean') return String(value)
  if (typeof value === 'object') {
    // If it's an object or array, convert to string representation
    if (Array.isArray(value)) {
      return value.map(v => renderValue(v)).join(', ')
    }
    // For objects, try to display meaningfully
    try {
      return JSON.stringify(value, null, 2)
    } catch {
      return String(value)
    }
  }
  return String(value)
}

// Helper function to safely get nested values
const safeGet = (obj, path, defaultValue = null) => {
  const result = path.split('.').reduce((current, prop) => current?.[prop], obj)
  return result !== undefined ? result : defaultValue
}

const IncidentResults = ({ result, onClear }) => {
  if (!result) {
    return (
      <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
        <p className="text-yellow-800">No analysis result available</p>
      </div>
    )
  }

  try {
    const {
      incident_id,
      summary,
      triage,
      analysis,
      root_cause,
      recommendations,
      post_incident_report
    } = result

    return (
      <div className="space-y-6">
        {/* Header */}
        <div className="bg-white rounded-lg shadow-sm border p-6">
          <div className="flex justify-between items-start mb-4">
            <div>
              <h2 className="text-2xl font-bold text-gray-900 mb-2">Incident Analysis Complete</h2>
            <p className="text-gray-600">Incident ID: {incident_id}</p>
          </div>
          <button
            onClick={onClear}
            className="bg-gray-100 text-gray-700 px-4 py-2 rounded-md hover:bg-gray-200 transition-colors"
          >
            New Analysis
          </button>
        </div>
        
        <div className="flex items-center space-x-4">
          <SeverityBadge severity={summary?.severity || triage?.severity} />
          <span className="text-lg font-medium text-gray-900">{summary?.title}</span>
        </div>
      </div>

      {/* Summary */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Executive Summary</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <h4 className="font-medium text-gray-700 mb-2">Affected Services</h4>
            <div className="space-y-1">
              {ensureArray(summary?.affected_services || triage?.affected_services).map((service, index) => (
                <span key={index} className="inline-block bg-red-100 text-red-800 px-2 py-1 rounded text-sm mr-2">
                  {renderValue(service)}
                </span>
              ))}
            </div>
          </div>
          <div>
            <h4 className="font-medium text-gray-700 mb-2">Business Impact</h4>
            <p className="text-gray-600">{triage?.business_impact}</p>
          </div>
        </div>
      </div>

      {/* Root Cause Analysis */}
      <div className="bg-white rounded-lg shadow-sm border p-6">
        <h3 className="text-lg font-semibold text-gray-900 mb-4">Root Cause Analysis</h3>
        <div className="space-y-4">
          <div>
            <h4 className="font-medium text-gray-700 mb-2">Primary Root Cause</h4>
            <p className="text-gray-900 bg-yellow-50 p-3 rounded border-l-4 border-yellow-400">
              {renderValue(root_cause?.primary_cause) || renderValue(summary?.root_cause)}
            </p>
          </div>
          
          {root_cause?.supporting_evidence && ensureArray(root_cause?.supporting_evidence).length > 0 && (
            <div>
              <h4 className="font-medium text-gray-700 mb-2">Supporting Evidence</h4>
              <ul className="list-disc list-inside space-y-1 text-gray-600">
                {ensureArray(root_cause?.supporting_evidence).map((evidence, index) => (
                  <li key={index}>{renderValue(evidence)}</li>
                ))}
              </ul>
            </div>
          )}

          {root_cause?.failure_chain && (
            <div>
              <h4 className="font-medium text-gray-700 mb-2">Failure Chain</h4>
              <p className="text-gray-600 bg-gray-50 p-3 rounded">{root_cause.failure_chain}</p>
            </div>
          )}
        </div>
      </div>

      {/* Analysis Details */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Log Analysis */}
        {analysis?.logs && (
          <div className="bg-white rounded-lg shadow-sm border p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Log Analysis</h3>
            <div className="space-y-3">
              {(() => {
                const errors = ensureArray(analysis.logs?.key_errors)
                return errors.length > 0 && (
                  <div>
                    <h4 className="font-medium text-gray-700 mb-2">Key Errors</h4>
                    <div className="space-y-1">
                      {errors.map((error, index) => (
                        <div key={index} className="bg-red-50 text-red-800 p-2 rounded text-sm font-mono">
                          {renderValue(error)}
                        </div>
                      ))}
                    </div>
                  </div>
                )
              })()}
              
              {(() => {
                const timeline = ensureArray(analysis.logs?.timeline)
                return timeline.length > 0 && (
                  <div>
                    <h4 className="font-medium text-gray-700 mb-2">Timeline</h4>
                    <div className="space-y-2">
                      {timeline.map((event, index) => (
                        <div key={index} className="flex items-center space-x-3 text-sm">
                          <span className="text-gray-500 font-mono">{renderValue(event?.timestamp) || 'N/A'}</span>
                          <span className={`px-2 py-1 rounded text-xs ${
                            event?.severity === 'ERROR' ? 'bg-red-100 text-red-800' : 'bg-yellow-100 text-yellow-800'
                          }`}>
                            {renderValue(event?.severity) || 'INFO'}
                          </span>
                          <span className="text-gray-700">{renderValue(event?.event) || 'Unknown'}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )
              })()}
            </div>
          </div>
        )}

        {/* Metrics Analysis */}
        {analysis?.metrics && (
          <div className="bg-white rounded-lg shadow-sm border p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Metrics Analysis</h3>
            <div className="space-y-3">
              {(() => {
                const breaches = ensureArray(analysis.metrics?.threshold_breaches)
                return breaches.length > 0 && (
                  <div>
                    <h4 className="font-medium text-gray-700 mb-2">Threshold Breaches</h4>
                    <div className="space-y-2">
                      {breaches.map((breach, index) => (
                        <div key={index} className="bg-red-50 p-3 rounded">
                          <div className="flex justify-between items-center">
                            <span className="font-medium text-red-800">{renderValue(breach?.metric) || 'Unknown Metric'}</span>
                            <span className={`px-2 py-1 rounded text-xs ${
                              breach?.severity === 'Critical' ? 'bg-red-100 text-red-800' : 'bg-yellow-100 text-yellow-800'
                            }`}>
                              {renderValue(breach?.severity) || 'Unknown'}
                            </span>
                          </div>
                          <div className="text-sm text-red-700 mt-1">
                            Current: {renderValue(breach?.value) || 'N/A'} | Threshold: {renderValue(breach?.threshold) || 'N/A'}
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                )
              })()}
              
              {(() => {
                const constraints = ensureArray(analysis.metrics?.resource_constraints)
                return constraints.length > 0 && (
                  <div>
                    <h4 className="font-medium text-gray-700 mb-2">Resource Constraints</h4>
                    <ul className="list-disc list-inside space-y-1 text-gray-600">
                      {constraints.map((constraint, index) => (
                        <li key={index}>{renderValue(constraint)}</li>
                      ))}
                    </ul>
                  </div>
                )
              })()}
            </div>
          </div>
        )}
      </div>

      {/* Recommendations */}
      {recommendations && (
        <div className="bg-white rounded-lg shadow-sm border p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Action Recommendations</h3>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {/* Immediate Actions */}
            {(() => {
              const immediateActions = ensureArray(recommendations?.immediate_actions)
              return immediateActions.length > 0 && (
                <div>
                  <h4 className="font-medium text-gray-700 mb-3">Immediate Actions</h4>
                  <div className="space-y-3">
                    {immediateActions.map((action, index) => (
                      <div key={index} className="border-l-4 border-red-400 bg-red-50 p-3">
                        <div className="flex justify-between items-start mb-1">
                          <span className="font-medium text-red-800">{renderValue(action?.action) || 'Action'}</span>
                          <span className={`px-2 py-1 rounded text-xs ${
                            action?.priority === 'High' ? 'bg-red-100 text-red-800' : 'bg-yellow-100 text-yellow-800'
                          }`}>
                            {renderValue(action?.priority) || 'Medium'}
                          </span>
                        </div>
                        <div className="text-sm text-red-700">ETA: {renderValue(action?.estimated_time) || 'TBD'}</div>
                      </div>
                    ))}
                  </div>
                </div>
              )
            })()}

            {/* Long-term Actions */}
            {(() => {
              const longTermActions = ensureArray(recommendations?.long_term_actions)
              return longTermActions.length > 0 && (
                <div>
                  <h4 className="font-medium text-gray-700 mb-3">Long-term Actions</h4>
                  <div className="space-y-3">
                    {longTermActions.map((action, index) => (
                      <div key={index} className="border-l-4 border-blue-400 bg-blue-50 p-3">
                        <div className="flex justify-between items-start mb-1">
                          <span className="font-medium text-blue-800">{renderValue(action?.action) || 'Action'}</span>
                          <span className={`px-2 py-1 rounded text-xs ${
                            action?.priority === 'High' ? 'bg-blue-100 text-blue-800' : 'bg-gray-100 text-gray-800'
                          }`}>
                            {renderValue(action?.priority) || 'Medium'}
                          </span>
                        </div>
                        <div className="text-sm text-blue-700">Effort: {renderValue(action?.estimated_effort) || 'TBD'}</div>
                      </div>
                    ))}
                  </div>
                </div>
              )
            })()}
          </div>
        </div>
      )}

      {/* Post-Incident Report */}
      {post_incident_report && (
        <div className="bg-white rounded-lg shadow-sm border p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Post-Incident Report</h3>
          <div className="space-y-4">
            {(() => {
              const keyTakeaways = ensureArray(post_incident_report?.key_takeaways)
              return keyTakeaways.length > 0 && (
                <div>
                  <h4 className="font-medium text-gray-700 mb-2">Key Takeaways</h4>
                  <ul className="list-disc list-inside space-y-1 text-gray-600">
                    {keyTakeaways.map((item, index) => (
                      <li key={index}>{renderValue(item)}</li>
                    ))}
                  </ul>
                </div>
              )
            })()}

            {(() => {
              const bestPractices = ensureArray(post_incident_report?.best_practices)
              return bestPractices.length > 0 && (
                <div>
                  <h4 className="font-medium text-gray-700 mb-2">Best Practices</h4>
                  <ul className="list-disc list-inside space-y-1 text-gray-600">
                    {bestPractices.map((item, index) => (
                      <li key={index}>{renderValue(item)}</li>
                    ))}
                  </ul>
                </div>
              )
            })()}
          </div>
        </div>
      )}
    </div>
    )
  } catch (error) {
    console.error('Error rendering incident results:', error)
    return (
      <div className="bg-red-50 border border-red-200 rounded-lg p-4">
        <h3 className="text-red-800 font-semibold mb-2">Error Displaying Results</h3>
        <p className="text-red-700 text-sm">{error.message}</p>
        <button
          onClick={onClear}
          className="mt-3 bg-red-600 text-white px-4 py-2 rounded-md hover:bg-red-700 transition-colors text-sm"
        >
          Clear and Try Again
        </button>
      </div>
    )
  }
}

export default IncidentResults