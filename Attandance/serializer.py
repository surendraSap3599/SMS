from rest_framework import serializers
from .models import Attendance, PeriodAttendance

class AttandanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'  

class PeriodAttandanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodAttendance
        fields = '__all__'  

