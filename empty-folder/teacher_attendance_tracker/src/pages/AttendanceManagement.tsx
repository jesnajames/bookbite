import AttendanceForm from '../components/attendance/AttendanceForm'
import StudentList from '../components/attendance/StudentList'

const AttendanceManagement = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Attendance Management</h1>
      <AttendanceForm />
      <StudentList />
    </div>
  )
}

export default AttendanceManagement
