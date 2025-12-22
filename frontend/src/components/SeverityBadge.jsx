import React from 'react'

const SeverityBadge = ({ severity }) => {
  const getSeverityStyles = (sev) => {
    switch (sev) {
      case 'P0':
        return 'bg-red-100 text-red-800 border-red-200'
      case 'P1':
        return 'bg-orange-100 text-orange-800 border-orange-200'
      case 'P2':
        return 'bg-yellow-100 text-yellow-800 border-yellow-200'
      case 'P3':
        return 'bg-green-100 text-green-800 border-green-200'
      default:
        return 'bg-gray-100 text-gray-800 border-gray-200'
    }
  }

  const getSeverityLabel = (sev) => {
    switch (sev) {
      case 'P0':
        return 'P0 - Critical'
      case 'P1':
        return 'P1 - High'
      case 'P2':
        return 'P2 - Medium'
      case 'P3':
        return 'P3 - Low'
      default:
        return 'Unknown'
    }
  }

  return (
    <span className={`inline-flex items-center px-3 py-1 rounded-full text-sm font-medium border ${getSeverityStyles(severity)}`}>
      {getSeverityLabel(severity)}
    </span>
  )
}

export default SeverityBadge