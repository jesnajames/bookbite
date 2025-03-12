import { Link } from 'react-router-dom'

const Sidebar = () => {
  return (
    <div className="w-64 bg-gray-100 min-h-screen p-4">
      <div className="flex flex-col gap-2">
        <Link to="/dashboard" className="p-2 hover:bg-gray-200 rounded">
          Dashboard
        </Link>
        <Link to="/attendance" className="p-2 hover:bg-gray-200 rounded">
          Take Attendance
        </Link>
        <Link to="/reports" className="p-2 hover:bg-gray-200 rounded">
          View Reports
        </Link>
      </div>
    </div>
  )
}

export default Sidebar
