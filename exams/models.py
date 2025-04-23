from django.db import models
from student.models import Student
from Acadamics.models import Level, Subject
from user.models import CustomUser

class Exam(models.Model):
    name = models.CharField(max_length=255)
    class_enrolled = models.ForeignKey(Level, on_delete=models.CASCADE)
    exam_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.exam_date}"

class MarksEntry(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2)
    entered_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    entry_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.marks_obtained}"

class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    total_marks = models.IntegerField(null=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)
    rank = models.IntegerField(null=True)
    entered_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    finalized_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='finalized_results')
    is_finalized = models.BooleanField(default=False)
    

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.marks_obtained}"
