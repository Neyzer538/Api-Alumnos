from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    activo = models.BooleanField()
    fechaMod = models.DateTimeField(auto_now_add=True)
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    genero = models.CharField(max_length=25)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    activo = models.BooleanField()
    fechaMod = models.DateTimeField(auto_now_add=True)
    
class Asignacion(models.Model):
    comentarios = models.CharField(max_length=300)
    activo = models.BooleanField()
    fechaMod = models.DateTimeField(auto_now_add=True)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="asignaciones")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name="asignacion")