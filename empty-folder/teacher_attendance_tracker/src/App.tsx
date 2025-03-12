import { Routes, Route } from 'react-router-dom'
import Login from './pages/Login'
import Dashboard from './pages/Dashboard'
import AttendanceManagement from './pages/AttendanceManagement'
import Reports from './pages/Reports'
import Navbar from './components/layout/Navbar'
import Footer from './components/layout/Footer'

function App() {
  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar />
      <main className="container mx-auto px-4 py-8">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/attendance" element={<AttendanceManagement />} />
          <Route path="/reports" element={<Reports />} />
        </Routes>
      </main>
      <Footer />
    </div>
  )
}

export default App
