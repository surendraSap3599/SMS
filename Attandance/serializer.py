from rest_framework import serializers
from .models import Attendance, PeriodAttendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'  

class PeriodAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodAttendance
        fields = '__all__'  

