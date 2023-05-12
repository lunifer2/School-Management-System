from django.urls import path
from .views import CourseListCreate,CourseRUD, StudentListCreate,TeacherSalaryListCreate,TeacherSalaryAllowanceRUD,TeacherSalaryAllowanceListCreate,TeacherSalaryRUD, StudentRUD,UserRegisterView ,UserLoginView ,SubjectRUD,SubjectListCreate, CourseOfStudentListCreate, CourseOfStudentRUD, TeacherListCreate, TeacherRUD, StudentFeeListCreate, StudentFeeRUD, SubjectOfTeacherListCreate, SubjectOfTeacherRUD


urlpatterns = [
    # path('course/', CourseApiView.as_view()),
    path('coursecreate/', CourseListCreate.as_view()),
    path('course/<int:pk>/', CourseRUD.as_view()),
    path('subject/', SubjectListCreate.as_view()),
    path('subject/<int:pk>/', SubjectRUD.as_view()),
    path('student/', StudentListCreate.as_view()),
    path('student/<int:pk>/', StudentRUD.as_view()),
    path('student/course/', CourseOfStudentListCreate.as_view()),
    path('student/course/<int:pk>/', CourseOfStudentRUD.as_view()),
    path('teacher/', TeacherListCreate.as_view()),
    path('teacher/<int:pk>/', TeacherRUD.as_view()),
    path('teacher/salary/', TeacherSalaryListCreate.as_view()),
    path('teacher/salary/<int:pk>/', TeacherSalaryRUD.as_view()),
    path('teacher/salary/allowance/', TeacherSalaryAllowanceListCreate.as_view()),
    path('teacher/salary/allowance/<int:pk>/', TeacherSalaryAllowanceRUD.as_view()),
    path('teacher/subject/', SubjectOfTeacherListCreate.as_view()),
    path('teacher/subject/<int:pk>/', SubjectOfTeacherRUD.as_view()),
    path('student/fee/', StudentFeeListCreate.as_view()),
    path('student/fee/<int:pk>/', StudentFeeRUD.as_view()),
    path('logins/', UserLoginView.as_view()),
    path('register/', UserRegisterView.as_view()),
]