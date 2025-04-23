from rest_framework.viewsets import ModelViewSet
from .models import Exam, MarksEntry, Result
from .serializer import ExamSerializer, MarksEntrySerializer, ResultSerializer

class ExamViewSet(ModelViewSet):
    queryset=Exam.objects.all()
    serializer_class=ExamSerializer

class MarksEntryViewSet(ModelViewSet):
    queryset=MarksEntry.objects.all()
    serializer_class=MarksEntrySerializer


class ResultViewSet(ModelViewSet):
    queryset=Result.objects.all()
    serializer_class=ResultSerializer
