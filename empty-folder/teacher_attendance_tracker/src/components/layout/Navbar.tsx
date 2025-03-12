import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <nav className="bg-blue-600 text-white">
      <div className="container mx-auto px-4 py-3 flex justify-between items-center">
        <Link to="/dashboard" className="text-xl font-bold">
          Teacher Portal
        </Link>
        <div className="flex gap-4">
          <Link to="/dashboard" className="hover:text-blue-200">Dashboard</Link>
          <Link to="/attendance" className="hover:text-blue-200">Attendance</Link>
          <Link to="/reports" className="hover:text-blue-200">Reports</Link>
          <button className="hover:text-blue-200">Logout</button>
        </div>
      </div>
    </nav>
  )
}

export default Navbar
