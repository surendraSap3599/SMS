from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Level, SubjectTeacher, Subject, Routine
from . serializer import LevelSerializer, SubjectSerializer, SubjectTeacherSerializer, RoutineSerializer



class LevelViewSet(ModelViewSet):
    queryset=Level.objects.all()
    serializer_class=LevelSerializer

class SubjectTeacherViewSet(ModelViewSet):
    queryset=SubjectTeacher.objects.all()
    serializer_class=SubjectTeacherSerializer

class SubjectViewSet(ModelViewSet):
    queryset=Subject.objects.all()
    serializer_class=SubjectSerializer
    
class RoutineViewSet(ModelViewSet):
    queryset=Routine.objects.all()
    serializer_class=RoutineSerializer