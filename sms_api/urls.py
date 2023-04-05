from django.urls import path
from .views import CourseApiView, CourseApiIdView, SubjectApiIdView, SubjectApiView, StudentApiIdView, StudentApiView, CourseOfStudentApiIdView, CourseOfStudentApiView, TeacherApiIdView, TeacherApiView,  TeacherSalaryApiIdView, TeacherSalaryApiView,TeacherSalaryAllowanceApiIdView, TeacherSalaryAllowanceApiView, SubjectOfTeacherApiIdView, SubjectOfTeacherApiView,StudentFeeApiIdView, StudentFeeApiView


urlpatterns = [
    path('course/', CourseApiView.as_view()),
    path('course/<int:id>/', CourseApiIdView.as_view()),
    path('subject/', SubjectApiView.as_view()),
    path('subject/<int:id>/', SubjectApiIdView.as_view()),
    path('student/', StudentApiView.as_view()),
    path('student/<int:id>/', StudentApiIdView.as_view()),
    path('student/course/', CourseOfStudentApiView.as_view()),
    path('student/course/<int:id>/', CourseOfStudentApiIdView.as_view()),
    path('teacher/', TeacherApiView.as_view()),
    path('teacher/<int:id>/', TeacherApiIdView.as_view()),
    path('teacher/salary/', TeacherSalaryApiView.as_view()),
    path('teacher/salary/<int:id>/', TeacherSalaryApiIdView.as_view()),
    path('teacher/salary/allowance/', TeacherSalaryAllowanceApiView.as_view()),
    path('teacher/salary/allowance/<int:id>/', TeacherSalaryAllowanceApiIdView.as_view()),
    path('teacher/subject/', SubjectOfTeacherApiView.as_view()),
    path('teacher/subject/<int:id>/', SubjectOfTeacherApiIdView.as_view()),
    path('student/fee/', StudentFeeApiView.as_view()),
    path('student/fee/<int:id>/', StudentFeeApiIdView.as_view()),
]