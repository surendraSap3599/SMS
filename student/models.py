from django.db import models
from user.models import CustomUser
from Acadamics.models import Level

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    admission_date = models.DateField()
    class_enrolled = models.ForeignKey(Level, on_delete=models.CASCADE)
    address = models.TextField()
    guardian_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.full_name

class Admission(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    admission_date = models.DateField()
    admitted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    remarks = models.TextField()

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_on = models.DateField()
    recorded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
