from django.shortcuts import render
from .models import Student, Exam


def students_list(request):
    students = Student.objects.all()
    return render(request, 'Students/students_list.html', {'students': students})


def student_scores(request, id):
    student = Student.objects.get(pk=id)
    scores = Exam.objects.filter(student=student)
    return render(request, 'Students/student_scores.html', {'student': student, 'scores': scores})
