import { useState, useEffect } from 'react'

interface Stats {
  totalStudents: number;
  presentToday: number;
  absentToday: number;
  averageAttendance: number;
}

const DashboardStats = () => {
  const [stats, setStats] = useState<Stats>({
    totalStudents: 0,
    presentToday: 0,
    absentToday: 0,
    averageAttendance: 0
  })

  useEffect(() => {
    // Mock data - replace with actual API call
    setStats({
      totalStudents: 45,
      presentToday: 40,
      absentToday: 5,
      averageAttendance: 92
    })
  }, [])

  return (
    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-gray-500 text-sm">Total Students</h3>
        <p className="text-3xl font-bold">{stats.totalStudents}</p>
      </div>
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-gray-500 text-sm">Present Today</h3>
        <p className="text-3xl font-bold text-green-600">{stats.presentToday}</p>
      </div>
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-gray-500 text-sm">Absent Today</h3>
        <p className="text-3xl font-bold text-red-600">{stats.absentToday}</p>
      </div>
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-gray-500 text-sm">Average Attendance</h3>
        <p className="text-3xl font-bold text-blue-600">{stats.averageAttendance}%</p>
      </div>
    </div>
  )
}

export default DashboardStats
