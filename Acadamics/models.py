from django.db import models
from user.models import CustomUser

class Level(models.Model):
    name = models.CharField(max_length=50)
    class_teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class SubjectTeacher(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    class_enrolled = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.teacher} - {self.subject}"

class Routine(models.Model):
    class_enrolled = models.ForeignKey(Level, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
