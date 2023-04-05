from django.contrib import admin
from .models import Teacher, Student, Course, Course_of_student, Subject, Student_fee, Subject_of_teacher, Teacher_salary, Teacher_salary_allowance
# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Course_of_student)
admin.site.register(Subject)
admin.site.register(Student_fee)
admin.site.register(Subject_of_teacher)
admin.site.register(Teacher_salary)
admin.site.register(Teacher_salary_allowance)
