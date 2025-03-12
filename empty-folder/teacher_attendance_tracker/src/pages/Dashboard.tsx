import DashboardStats from '../components/dashboard/DashboardStats'
import ClassList from '../components/dashboard/ClassList'

const Dashboard = () => {
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Dashboard</h1>
      <DashboardStats />
      <ClassList />
    </div>
  )
}

export default Dashboard
