import React from 'react'
import SeverityBadge from './SeverityBadge'

const IncidentResults = ({ result, onClear }) => {
  if (!result) return null

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
              {(summary?.affected_services || triage?.affected_services || []).map((service, index) => (
                <span key={index} className="inline-block bg-red-100 text-red-800 px-2 py-1 rounded text-sm mr-2">
                  {service}
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
              {root_cause?.primary_cause || summary?.root_cause}
            </p>
          </div>
          
          {root_cause?.supporting_evidence && (
            <div>
              <h4 className="font-medium text-gray-700 mb-2">Supporting Evidence</h4>
              <ul className="list-disc list-inside space-y-1 text-gray-600">
                {root_cause.supporting_evidence.map((evidence, index) => (
                  <li key={index}>{evidence}</li>
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
              {analysis.logs.key_errors && (
                <div>
                  <h4 className="font-medium text-gray-700 mb-2">Key Errors</h4>
                  <div className="space-y-1">
                    {analysis.logs.key_errors.map((error, index) => (
                      <div key={index} className="bg-red-50 text-red-800 p-2 rounded text-sm font-mono">
                        {error}
                      </div>
                    ))}
                  </div>
                </div>
              )}
              
              {analysis.logs.timeline && (
                <div>
                  <h4 className="font-medium text-gray-700 mb-2">Timeline</h4>
                  <div className="space-y-2">
                    {analysis.logs.timeline.map((event, index) => (
                      <div key={index} className="flex items-center space-x-3 text-sm">
                        <span className="text-gray-500 font-mono">{event.timestamp}</span>
                        <span className={`px-2 py-1 rounded text-xs ${
                          event.severity === 'ERROR' ? 'bg-red-100 text-red-800' : 'bg-yellow-100 text-yellow-800'
                        }`}>
                          {event.severity}
                        </span>
                        <span className="text-gray-700">{event.event}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </div>
        )}

        {/* Metrics Analysis */}
        {analysis?.metrics && (
          <div className="bg-white rounded-lg shadow-sm border p-6">
            <h3 className="text-lg font-semibold text-gray-900 mb-4">Metrics Analysis</h3>
            <div className="space-y-3">
              {analysis.metrics.threshold_breaches && (
                <div>
                  <h4 className="font-medium text-gray-700 mb-2">Threshold Breaches</h4>
                  <div className="space-y-2">
                    {analysis.metrics.threshold_breaches.map((breach, index) => (
                      <div key={index} className="bg-red-50 p-3 rounded">
                        <div className="flex justify-between items-center">
                          <span className="font-medium text-red-800">{breach.metric}</span>
                          <span className={`px-2 py-1 rounded text-xs ${
                            breach.severity === 'Critical' ? 'bg-red-100 text-red-800' : 'bg-yellow-100 text-yellow-800'
                          }`}>
                            {breach.severity}
                          </span>
                        </div>
                        <div className="text-sm text-red-700 mt-1">
                          Current: {breach.value} | Threshold: {breach.threshold}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
              
              {analysis.metrics.resource_constraints && (
                <div>
                  <h4 className="font-medium text-gray-700 mb-2">Resource Constraints</h4>
                  <ul className="list-disc list-inside space-y-1 text-gray-600">
                    {analysis.metrics.resource_constraints.map((constraint, index) => (
                      <li key={index}>{constraint}</li>
                    ))}
                  </ul>
                </div>
              )}
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
            {recommendations.immediate_actions && (
              <div>
                <h4 className="font-medium text-gray-700 mb-3">Immediate Actions</h4>
                <div className="space-y-3">
                  {recommendations.immediate_actions.map((action, index) => (
                    <div key={index} className="border-l-4 border-red-400 bg-red-50 p-3">
                      <div className="flex justify-between items-start mb-1">
                        <span className="font-medium text-red-800">{action.action}</span>
                        <span className={`px-2 py-1 rounded text-xs ${
                          action.priority === 'High' ? 'bg-red-100 text-red-800' : 'bg-yellow-100 text-yellow-800'
                        }`}>
                          {action.priority}
                        </span>
                      </div>
                      <div className="text-sm text-red-700">ETA: {action.estimated_time}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}

            {/* Long-term Actions */}
            {recommendations.long_term_actions && (
              <div>
                <h4 className="font-medium text-gray-700 mb-3">Long-term Actions</h4>
                <div className="space-y-3">
                  {recommendations.long_term_actions.map((action, index) => (
                    <div key={index} className="border-l-4 border-blue-400 bg-blue-50 p-3">
                      <div className="flex justify-between items-start mb-1">
                        <span className="font-medium text-blue-800">{action.action}</span>
                        <span className={`px-2 py-1 rounded text-xs ${
                          action.priority === 'High' ? 'bg-blue-100 text-blue-800' : 'bg-gray-100 text-gray-800'
                        }`}>
                          {action.priority}
                        </span>
                      </div>
                      <div className="text-sm text-blue-700">Effort: {action.estimated_effort}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Post-Incident Report */}
      {post_incident_report && (
        <div className="bg-white rounded-lg shadow-sm border p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-4">Post-Incident Report</h3>
          <div className="space-y-4">
            {post_incident_report.lessons_learned && (
              <div>
                <h4 className="font-medium text-gray-700 mb-2">Lessons Learned</h4>
                <ul className="list-disc list-inside space-y-1 text-gray-600">
                  {post_incident_report.lessons_learned.map((lesson, index) => (
                    <li key={index}>{lesson}</li>
                  ))}
                </ul>
              </div>
            )}
            
            {post_incident_report.preventive_measures && (
              <div>
                <h4 className="font-medium text-gray-700 mb-2">Preventive Measures</h4>
                <ul className="list-disc list-inside space-y-1 text-gray-600">
                  {post_incident_report.preventive_measures.map((measure, index) => (
                    <li key={index}>{measure}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  )
}

export default IncidentResults