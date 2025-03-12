import { useState, useEffect } from 'react'
import { Class } from '../../types/class'
import { Link } from 'react-router-dom'

const ClassList = () => {
  const [classes, setClasses] = useState<Class[]>([])

  useEffect(() => {
    // Mock data - replace with actual API call
    setClasses([
      {
        id: '1',
        name: 'Mathematics 101',
        teacherId: 'teacher1',
        schedule: 'Mon, Wed 9:00 AM',
        students: ['1', '2', '3']
      },
      {
        id: '2',
        name: 'Physics 101',
        teacherId: 'teacher1',
        schedule: 'Tue, Thu 10:00 AM',
        students: ['1', '2', '4']
      }
    ])
  }, [])

  return (
    <div className="bg-white rounded-lg shadow">
      <div className="p-6">
        <h2 className="text-xl font-semibold mb-4">Your Classes</h2>
        <div className="grid gap-4">
          {classes.map((classItem) => (
            <div key={classItem.id} className="border p-4 rounded-lg hover:bg-gray-50">
              <div className="flex justify-between items-center">
                <div>
                  <h3 className="font-semibold">{classItem.name}</h3>
                  <p className="text-gray-600">{classItem.schedule}</p>
                  <p className="text-sm text-gray-500">{classItem.students.length} students</p>
                </div>
                <Link
                  to={`/attendance?classId=${classItem.id}`}
                  className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
                >
                  Take Attendance
                </Link>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

export default ClassList
