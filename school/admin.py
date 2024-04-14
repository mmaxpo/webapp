from django.contrib import admin

from school.models import Student, Course, Enrollment


class EnrollmentInline(admin.TabularInline):
    model = Enrollment
    extra = 1


@admin.register(Student)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_of_birth']
    inlines = [EnrollmentInline]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'grade', 'date_of_enrollment']
