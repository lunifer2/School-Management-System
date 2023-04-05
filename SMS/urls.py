from django.urls import path
from . import views
from .views import Course_add_View, Student_add_View, Student_fee_View, Teacher_add_View, Teacher_add_salary_View, Subject_add_View, Teacher_assign_subject_View

urlpatterns = [
    path("index/", views.courses_index, name = 'index-course'),
    path("courses/add", Course_add_View.as_view(), name ='add-course' ),
    path("courses/delete/<int:id>", views.courses_delete, name = 'delete-course'),
    path("students/add", Student_add_View.as_view(), name = 'add-student'),
    path("students/index",views.students_index, name='index-student' ),
    path("students/delete/<int:id>", views.students_delete, name= 'delete-student'),
    path("students/view/<int:id>",views.students_view, name='view-student'),
    path("students/edit/<int:id>",views.students_edit, name='edit-student'),
    path("students/update/",views.students_update, name='update-student'),
    path("students/fee",Student_fee_View.as_view(), name = 'fee-student'),
    path("students/fee/index",views.students_fee_index, name = 'fee-index-student'),
    path("teachers/add", Teacher_add_View.as_view(), name = 'add-teacher'),
    path("teachers/assign", Teacher_assign_subject_View.as_view(), name = 'add-teacher-subject'),
    path("teachers/index", views.teachers_index, name = 'index-teacher'),
    path("teachers/delete/<int:id>", views.teachers_delete, name= 'delete-teacher'),
    path("teachers/view/<int:id>",views.teachers_view, name='view-teacher'),
    path("teachers/edit/<int:id>",views.teachers_edit, name='edit-teacher'),
    path("teachers/update/",views.teachers_update, name='update-teacher'),
    path("teachers/salary",views.teachers_salary, name = 'salary-teacher'),
    path("teachers/salary/add",Teacher_add_salary_View.as_view(), name = 'add-salary-teacher'),
    path("subjects/add",Subject_add_View.as_view(), name = 'add-subject'),
    path("subjects/index",views.subjects_index, name = 'index-subject')

    ]   