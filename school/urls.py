from django.urls import path

from school.views import *

urlpatterns = [
    path('student_list/', student_list, name='student_list'),
    path('register_student/', register_student, name='register_student'),
    path('student_details/<int:pk>/', student_details, name='student_details'),
    path('student_search/', student_search, name='student_search'),
    path('remove_student_course/<int:pk>', student_remove, name='remove_student'),

]
