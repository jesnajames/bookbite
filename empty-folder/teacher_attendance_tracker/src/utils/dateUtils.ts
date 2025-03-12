export const formatDate = (date: Date): string => {
  return date.toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

export const getCurrentWeek = (): Date[] => {
  const today = new Date()
  const week = []
  for (let i = 0; i < 7; i++) {
    const day = new Date(today)
    day.setDate(today.getDate() - today.getDay() + i)
    week.push(day)
  }
  return week
}
