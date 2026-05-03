from django.urls import path
from .views import ListaAlumnoView, AlumnoDetalleView, ListaCursoView, CursoDetalleView, ListaAsignacionView, AsignacionDetalleView

urlpatterns = [
    path('alumnos/', ListaAlumnoView.as_view(), name='Lista-Alumnos'),
    path('alumnos/<int:pk>/', AlumnoDetalleView.as_view(), name='Detalle-Alumno'),
    path('cursos/', ListaCursoView.as_view(), name='Lista-Cursos'),
    path('cursos/<int:pk>/', CursoDetalleView.as_view(), name='Detalle-Curso'),
    path('asignaciones/', ListaAsignacionView.as_view(), name='Lista-Asignaciones'),
    path('asignaciones/<int:pk>/', AsignacionDetalleView.as_view(), name='Detalle-Asignacion'),
]
