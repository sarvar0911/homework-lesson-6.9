from django.urls import path
from . import views

urlpatterns = [
    path('', views.students_list, name='students_list'),
    path('<int:id>/', views.student_scores, name='student_scores'),
]
