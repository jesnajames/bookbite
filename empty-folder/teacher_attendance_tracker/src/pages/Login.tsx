import LoginForm from '../components/auth/LoginForm'

const Login = () => {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
        <h1 className="text-2xl font-bold mb-6 text-center">Teacher Login</h1>
        <LoginForm />
      </div>
    </div>
  )
}

export default Login
