from django.db import models
from student.models import Student
from Acadamics.models import Level, Subject
from user.models import CustomUser

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])
    marked_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"

class PeriodAttendance(models.Model):
    class_enrolled = models.ForeignKey(Level, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendance_date = models.DateField()
    period_number = models.IntegerField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.attendance_date} - Period {self.period_number} - {self.status}"
