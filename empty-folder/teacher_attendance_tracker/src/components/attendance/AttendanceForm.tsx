import { useState } from 'react'
import { Student } from '../../types/student'
import { AttendanceRecord } from '../../types/attendance'

const AttendanceForm = () => {
  const [selectedDate, setSelectedDate] = useState(new Date().toISOString().split('T')[0])
  const [selectedClass, setSelectedClass] = useState('')
  const [attendanceRecords, setAttendanceRecords] = useState<Record<string, 'present' | 'absent' | 'late'>>({})

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // Handle submission logic
    console.log({ selectedDate, selectedClass, attendanceRecords })
  }

  return (
    <div className="bg-white p-6 rounded-lg shadow">
      <form onSubmit={handleSubmit}>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
          <div>
            <label className="block mb-2">Date</label>
            <input
              type="date"
              value={selectedDate}
              onChange={(e) => setSelectedDate(e.target.value)}
              className="w-full p-2 border rounded"
            />
          </div>
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
        </div>
        <button
          type="submit"
          className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700"
        >
          Save Attendance
        </button>
      </form>
    </div>
  )
}

export default AttendanceForm
