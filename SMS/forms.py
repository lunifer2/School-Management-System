from django import forms
from .models import Course, Course_of_student, Student, Student_fee, Subject, Subject_of_teacher, Teacher_salary, Teacher_salary_allowance, Teacher


class CourseCreateForm(forms.ModelForm):
    """ Form Class for Course Creation """
    class Meta:
        fields = "__all__"
        model = Course


class StudentRegistrationForm(forms.ModelForm):
    """ Form class for student registration """
    class Meta:
        fields = "__all__"
        model = Student


class SubjectCreationForm(forms.ModelForm):
    """ Form class for subject creation """
    class Meta:
        fields = "__all__"
        model = Subject


class TeacherRegistrationForm(forms.ModelForm):
    """ Form class for teacher registration """
    class Meta:
        fields = "__all__"
        model = Teacher


class TeacherSalaryForm(forms.ModelForm):
    """ Form class to add teacher's salary """
    class Meta:
        fields = "__all__"
        model = Teacher_salary


class TeacherSalaryScaleForm(forms.ModelForm):
    """ Form class to add salary scale """
    class Meta:
        fields = "__all__"
        model = Teacher_salary_allowance


class StudentFeeForm(forms.ModelForm):
    """ Form class to add student's fee """
    class Meta:
        fields = "__all__"
        model = Student_fee


class TeacherSubjectCreationForm(forms.ModelForm):
    """ Form class to assign subjects to teacher """
    class Meta:
        fields = "__all__"
        model = Subject_of_teacher
