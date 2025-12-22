/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'sre-blue': '#1e40af',
        'sre-red': '#dc2626',
        'sre-yellow': '#d97706',
        'sre-green': '#059669',
      }
    },
  },
  plugins: [],
}