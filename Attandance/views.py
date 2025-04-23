from rest_framework.viewsets import ModelViewSet
from .models import Attendance, PeriodAttendance
from .serializer import AttendanceSerializer, PeriodAttendanceSerializer


class AttendanceViewSet(ModelViewSet):
    queryset= Attendance.objects.all()
    serializer_class=AttendanceSerializer

class PeriodAttendanceViewSet(ModelViewSet):
    queryset=PeriodAttendance.objects.all()
    serializer_class=PeriodAttendanceSerializer