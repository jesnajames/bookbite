import { useState, useEffect } from 'react'
import { AttendanceRecord } from '../../types/attendance'
import { formatDate } from '../../utils/dateUtils'

const AttendanceReport = () => {
  const [reports, setReports] = useState<AttendanceRecord[]>([])
  const [selectedClass, setSelectedClass] = useState('')
  const [dateRange, setDateRange] = useState({
    start: new Date().toISOString().split('T')[0],
    end: new Date().toISOString().split('T')[0]
  })

  const handleGenerateReport = () => {
    // Mock data - replace with actual API call
    setReports([
      {
        id: '1',
        classId: '1',
        studentId: '1',
        date: '2024-01-15',
        status: 'present'
      },
      {
        id: '2',
        classId: '1',
        studentId: '2',
        date: '2024-01-15',
        status: 'absent'
      }
    ])
  }

  return (
    <div className="bg-white rounded-lg shadow">
      <div className="p-6">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
          <div>
            <label className="block mb-2">Class</label>
            <select
              value={selectedClass}
              onChange={(e) => setSelectedClass(e.target.value)}
              className="w-full p-2 border rounded"
            >
              <option value="">Select Class</option>
              <option value="1">Mathematics 101</option>
              <option value="2">Physics 101</option>
            </select>
          </div>
          <div>
            <label className="block mb-2">Start Date</label>
            <input
              type="date"
              value={dateRange.start}
              onChange={(e) => setDateRange(prev => ({ ...prev, start: e.target.value }))}
              className="w-full p-2 border rounded"
            />
          </div>
          <div>
            <label className="block mb-2">End Date</label>
            <input
              type="date"
              value={dateRange.end}
              onChange={(e) => setDateRange(prev => ({ ...prev, end: e.target.value }))}
              className="w-full p-2 border rounded"
            />
          </div>
        </div>
        <button
          onClick={handleGenerateReport}
          className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
        >
          Generate Report
        </button>

        {reports.length > 0 && (
          <div className="mt-6">
            <h3 className="text-lg font-semibold mb-4">Attendance Report</h3>
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead>
                  <tr className="bg-gray-50">
                    <th className="px-6 py-3 text-left">Date</th>
                    <th className="px-6 py-3 text-left">Student ID</th>
                    <th className="px-6 py-3 text-left">Status</th>
                  </tr>
                </thead>
                <tbody>
                  {reports.map((record) => (
                    <tr key={record.id} className="border-t">
                      <td className="px-6 py-4">{record.date}</td>
                      <td className="px-6 py-4">{record.studentId}</td>
                      <td className="px-6 py-4">
                        <span className={`capitalize ${
                          record.status === 'present' ? 'text-green-600' :
                          record.status === 'absent' ? 'text-red-600' : 'text-yellow-600'
                        }`}>
                          {record.status}
                        </span>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        )}
      </div>
    </div>
  )
}

export default AttendanceReport
