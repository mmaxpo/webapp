from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from blog.models import Auther
from school.forms import RegisterStudentForm, StudentSearchForm
from school.models import Student, Course, Enrollment
from blog.serializers import AutherSerializer


def student_list(request):
    students = Student.objects.all()
    return render(request, 'school/student_list.html', {'students': students})


def register_student(request):
    if request.method == 'POST':
        form = RegisterStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/school/student_list')
        else:
            print(form.errors)
    else:
        form = RegisterStudentForm()
    return render(request, 'school/register_student.html', {'form': form})


def student_details(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'school/details_student.html', {'student': student})


def student_search(request):
    form = StudentSearchForm()
    results = []
    if 'query' in request.GET:
        form = StudentSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Student.objects.filter(Q(name__icontains=query))
    return render(request, 'school/search_student.html', {'form': form, 'results': results})


def student_remove(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return HttpResponseRedirect('/school/student_list/')


class AutherApiView(APIView):
    def get(self, request, *args, **kwargs):
        authers = Auther.objects.all()
        serializer = AutherSerializer(authers, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = AutherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)