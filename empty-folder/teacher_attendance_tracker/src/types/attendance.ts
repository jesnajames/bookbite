export interface AttendanceRecord {
  id: string;
  classId: string;
  studentId: string;
  date: string;
  status: 'present' | 'absent' | 'late';
  notes?: string;
}
