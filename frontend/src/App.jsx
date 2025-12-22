import React, { useState } from 'react'
import axios from 'axios'
import IncidentForm from './components/IncidentForm'
import IncidentResults from './components/IncidentResults'
import Header from './components/Header'
import LoadingSpinner from './components/LoadingSpinner'

const API_BASE_URL = 'https://work-1-sfkangrnyhsxayqz.prod-runtime.all-hands.dev'

function App() {
  const [analysisResult, setAnalysisResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleAnalyzeIncident = async (incidentData) => {
    setLoading(true)
    setError(null)
    setAnalysisResult(null)

    try {
      const response = await axios.post(`${API_BASE_URL}/analyze-incident`, incidentData, {
        headers: {
          'Content-Type': 'application/json',
        },
        timeout: 120000, // 2 minute timeout for LLM processing
      })

      setAnalysisResult(response.data.analysis)
    } catch (err) {
      console.error('Analysis error:', err)
      setError(
        err.response?.data?.detail || 
        err.message || 
        'Failed to analyze incident. Please check if the backend is running and Ollama is available.'
      )
    } finally {
      setLoading(false)
    }
  }

  const handleAnalyzeSample = async () => {
    setLoading(true)
    setError(null)
    setAnalysisResult(null)

    try {
      const response = await axios.post(`${API_BASE_URL}/analyze-sample`, {}, {
        headers: {
          'Content-Type': 'application/json',
        },
        timeout: 120000,
      })

      setAnalysisResult(response.data.analysis)
    } catch (err) {
      console.error('Sample analysis error:', err)
      setError(
        err.response?.data?.detail || 
        err.message || 
        'Failed to analyze sample incident. Please check if the backend is running and Ollama is available.'
      )
    } finally {
      setLoading(false)
    }
  }

  const handleClearResults = () => {
    setAnalysisResult(null)
    setError(null)
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <Header />
      
      <main className="container mx-auto px-4 py-8">
        <div className="max-w-6xl mx-auto">
          {/* Error Display */}
          {error && (
            <div className="mb-6 bg-red-50 border border-red-200 rounded-lg p-4">
              <div className="flex">
                <div className="flex-shrink-0">
                  <svg className="h-5 w-5 text-red-400" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z" clipRule="evenodd" />
                  </svg>
                </div>
                <div className="ml-3">
                  <h3 className="text-sm font-medium text-red-800">Analysis Error</h3>
                  <div className="mt-2 text-sm text-red-700">
                    <p>{error}</p>
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Loading State */}
          {loading && <LoadingSpinner />}

          {/* Main Content */}
          {!loading && !analysisResult && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <div>
                <IncidentForm onSubmit={handleAnalyzeIncident} />
              </div>
              <div className="bg-white rounded-lg shadow-sm border p-6">
                <h2 className="text-xl font-semibold text-gray-900 mb-4">Quick Demo</h2>
                <p className="text-gray-600 mb-4">
                  Try the system with a pre-loaded sample incident that demonstrates
                  a memory leak scenario with realistic alerts, logs, and metrics.
                </p>
                <button
                  onClick={handleAnalyzeSample}
                  className="w-full bg-sre-blue text-white px-4 py-2 rounded-md hover:bg-blue-700 transition-colors"
                >
                  Analyze Sample Incident
                </button>
              </div>
            </div>
          )}

          {/* Results */}
          {!loading && analysisResult && (
            <IncidentResults 
              result={analysisResult} 
              onClear={handleClearResults}
            />
          )}
        </div>
      </main>
    </div>
  )
}

export default App