from rest_framework.viewsets import ModelViewSet
from .models import Student, Admission, Fee
from .serializer import StudentSerializer, AdmissionSerializer, FeeSerializer

class StudentViewSet(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class= StudentSerializer

class AdmissionViewSet(ModelViewSet):
    queryset=Admission.objects.all()
    serializer_class=AdmissionSerializer

class FeeViewSet(ModelViewSet):
    queryset=Fee.objects.all()
    serializer_class=FeeSerializer