import { useState, useEffect } from 'react'
import { Student } from '../../types/student'

const StudentList = () => {
  const [students, setStudents] = useState<Student[]>([])
  const [attendance, setAttendance] = useState<Record<string, 'present' | 'absent' | 'late'>>({})

  useEffect(() => {
    // Mock data - replace with actual API call
    setStudents([
      { id: '1', firstName: 'John', lastName: 'Doe', email: 'john@example.com', classIds: ['1'] },
      { id: '2', firstName: 'Jane', lastName: 'Smith', email: 'jane@example.com', classIds: ['1'] }
    ])
  }, [])

  const handleAttendanceChange = (studentId: string, status: 'present' | 'absent' | 'late') => {
    setAttendance(prev => ({ ...prev, [studentId]: status }))
  }

  return (
    <div className="bg-white rounded-lg shadow mt-6">
      <div className="p-6">
        <h2 className="text-xl font-semibold mb-4">Student List</h2>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr className="bg-gray-50">
                <th className="px-6 py-3 text-left">Name</th>
                <th className="px-6 py-3 text-left">Status</th>
                <th className="px-6 py-3 text-left">Notes</th>
              </tr>
            </thead>
            <tbody>
              {students.map((student) => (
                <tr key={student.id} className="border-t">
                  <td className="px-6 py-4">
                    {student.firstName} {student.lastName}
                  </td>
                  <td className="px-6 py-4">
                    <select
                      value={attendance[student.id] || ''}
                      onChange={(e) => handleAttendanceChange(student.id, e.target.value as 'present' | 'absent' | 'late')}
                      className="border rounded p-1"
                    >
                      <option value="">Select</option>
                      <option value="present">Present</option>
                      <option value="absent">Absent</option>
                      <option value="late">Late</option>
                    </select>
                  </td>
                  <td className="px-6 py-4">
                    <input
                      type="text"
                      placeholder="Add notes"
                      className="border rounded p-1 w-full"
                    />
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}

export default StudentList
