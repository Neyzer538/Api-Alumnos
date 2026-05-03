from django.shortcuts import render
from rest_framework import generics
from .models import Alumno, Curso, Asignacion
from .serializer import AlumnoSerializer, CursoSerializer, AsignacionSerializer

# Create your views here.
class ListaAlumnoView(generics.ListCreateAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class AlumnoDetalleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    
class ListaCursoView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class CursoDetalleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    
class ListaAsignacionView(generics.ListCreateAPIView):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer
    
class AsignacionDetalleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asignacion.objects.all()
    serializer_class = AsignacionSerializer