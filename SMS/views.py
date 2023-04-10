from django.shortcuts import render, redirect
from .forms import CourseCreateForm, StudentRegistrationForm, StudentFeeForm, TeacherRegistrationForm, TeacherSubjectCreationForm, TeacherSalaryForm, TeacherSalaryScaleForm, SubjectCreationForm
from .models import Course, Student, Teacher, Teacher_salary, Teacher_salary_allowance, Subject, Student_fee, Subject_of_teacher, Course_of_student
from django.views import View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def courses_index(request):
    """ Returns the list of courses """
    course_list = Course.objects.all()
    context = {"data": course_list}
    if request.method == "POST":
        search = request.POST.get('search')
        courses = Course.objects.filter(course_name__icontains=search)
        context = {"data": courses}
        return render(request, 'courses/courses_index.html', context)
    return render(request, 'courses/courses_index.html', context)


@login_required(login_url='login')
def courses_delete(request, id):
    """ Deletes the courses """
    data = Course.objects.get(id=id)
    data.delete()
    return redirect("index-course")


class Course_add_View(View):
    """ This class adds the course """

    def get(self, request):
        if request.user.is_authenticated:
            course_create_form = CourseCreateForm()
            context = {"form": course_create_form}
            return render(request, 'courses/add_course.html', context)
        return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
            course = Course()
            course.course_code = request.POST.get('course_code')
            course.course_name = request.POST.get('course_name')
            course.semester_or_year = request.POST.get('semester_or_year')
            course.no_of_year = request.POST.get('no_of_year')
            course.save()
            return redirect('index-course')
        return redirect('/login/')


class Student_add_View(View):
    """ This class adds students """

    def get(self, request):
        if request.user.is_authenticated:
            student_create_form = StudentRegistrationForm()
            context = {"form": student_create_form}
            return render(request, 'students/add_student.html', context)
        return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
            student = Student()
            course_name = Course.objects.get(
                id=request.POST.get('course_name'))
            student.roll_no = request.POST.get('roll_no')
            student.first_name = request.POST.get('first_name')
            student.middle_name = request.POST.get('middle_name')
            student.last_name = request.POST.get('last_name')
            student.father_name = request.POST.get('father_name')
            student.mobile_no = request.POST.get('mobile_no')
            student.session = request.POST.get('session')
            student.applicant_status = request.POST.get('applicant_status')
            student.application_status = request.POST.get('application_status')
            student.dob = request.POST.get('dob')
            student.gender = request.POST.get('gender')
            student.address = request.POST.get('address')
            student.admission_date = request.POST.get('admission_date')
            student.email = request.POST.get('email')
            student.course_name = course_name
            student.save()

            return redirect('index-student')
        return redirect('/login/')


@login_required(login_url='login')
def students_index(request):
    """ Returns the list of students """
    student_list = Student.objects.all()
    context = {"data": student_list}
    if request.method == "POST":
        search = request.POST.get('search')
        students = Student.objects.filter(first_name__icontains=search)
        context = {"data": students}
        return render(request, 'students/student_index.html', context)
    return render(request, 'students/student_index.html', context)


@login_required(login_url='login')
def students_delete(request, id):
    """ Deletes the students """
    data = Student.objects.get(id=id)
    data.delete()
    return redirect("index-student")


@login_required(login_url='login')
def students_view(request, id):
    """ Shows the profile of a student """
    data = Student.objects.get(id=id)
    context = {"data": data}
    return render(request, 'students/view_student.html', context)


@login_required(login_url='login')
def students_edit(request, id):
    """ Edits the profile of a student """
    data = Student.objects.get(id=id)
    course = Course.objects.all()
    context = {"data": data, "course": course}

    return render(request, 'students/edit_student.html', context)


@login_required(login_url='login')
def students_update(request):
    if request.method == "POST":
        student = Student.objects.get(id=request.POST.get('id'))
        course_name = Course.objects.get(id=request.POST.get('course'))
        student.roll_no = request.POST.get('roll_no')
        student.first_name = request.POST.get('first_name')
        student.middle_name = request.POST.get('middle_name')
        student.last_name = request.POST.get('last_name')
        student.father_name = request.POST.get('father_name')
        student.mobile_no = request.POST.get('mobile_no')
        student.session = request.POST.get('session')
        student.applicant_status = request.POST.get('applicant_status')
        student.application_status = request.POST.get('application_status')
        student.dob = request.POST.get('dob')
        student.gender = request.POST.get('gender')
        student.address = request.POST.get('address')
        student.admission_date = request.POST.get('admission_date')
        student.email = request.POST.get('email')
        student.course_name = course_name
        student.save()

    return redirect('index-student')


class Teacher_add_View(View):
    """ This view adds teacher """

    def get(self, request):
        if request.user.is_authenticated:
            teacher_create_form = TeacherRegistrationForm()
            context = {"form": teacher_create_form}
            return render(request, 'teachers/add_teacher.html', context)
        return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
            teacher = Teacher()
            course_name = Course.objects.get(
                id=request.POST.get('course_name'))
            teacher.first_name = request.POST.get('first_name')
            teacher.middle_name = request.POST.get('middle_name')
            teacher.last_name = request.POST.get('last_name')
            teacher.mobile_no = request.POST.get('mobile_no')
            teacher.session = request.POST.get('session')
            teacher.teacher_status = request.POST.get('teacher_status')
            teacher.application_status = request.POST.get('application_status')
            teacher.dob = request.POST.get('dob')
            teacher.gender = request.POST.get('gender')
            teacher.address = request.POST.get('address')
            teacher.hire_date = request.POST.get('hire_date')
            teacher.email = request.POST.get('email')
            teacher.course_name = course_name
            teacher.save()

            return redirect('index-teacher')
        return redirect('/login/')


@login_required(login_url='login')
def teachers_index(request):
    """ Returns the list of teachers """
    teachers_list = Teacher.objects.all()
    context = {"data": teachers_list}
    if request.method == "POST":
        search = request.POST.get('search')
        teachers = Teacher.objects.filter(first_name__icontains=search)
        context = {"data": teachers}
        return render(request, 'teachers/teacher_index.html', context)
    return render(request, 'teachers/teacher_index.html', context)


@login_required(login_url='login')
def teachers_delete(request, id):
    """ Deletes the teachers """
    data = Teacher.objects.get(id=id)
    data.delete()
    return redirect("index-teacher")


@login_required(login_url='login')
def teachers_view(request, id):
    """ Shows the profile of a Teacher """
    data = Teacher.objects.get(id=id)
    context = {"data": data}
    return render(request, 'teachers/view_teacher.html', context)


@login_required(login_url='login')
def teachers_edit(request, id):
    """ Edits the profile of a teacher """
    data = Teacher.objects.get(id=id)
    course = Course.objects.all()
    context = {"data": data, "course": course}

    return render(request, 'teachers/edit_teacher.html', context)


@login_required(login_url='login')
def teachers_update(request):
    if request.method == "POST":
        teacher = Teacher.objects.get(id=request.POST.get('id'))
        course_name = Course.objects.get(id=request.POST.get('course_name'))
        teacher.first_name = request.POST.get('first_name')
        teacher.middle_name = request.POST.get('middle_name')
        teacher.last_name = request.POST.get('last_name')
        teacher.mobile_no = request.POST.get('mobile_no')
        teacher.session = request.POST.get('session')
        teacher.teacher_status = request.POST.get('teacher_status')
        teacher.application_status = request.POST.get('application_status')
        teacher.dob = request.POST.get('dob')
        teacher.gender = request.POST.get('gender')
        teacher.address = request.POST.get('address')
        teacher.hire_date = request.POST.get('hire_date')
        teacher.email = request.POST.get('email')
        teacher.course_name = course_name
        teacher.save()

    return redirect('index-teacher')


class Teacher_add_salary_View(View):
    """ This view adds salary of teacher """

    def get(self, request):
        if request.user.is_authenticated:
            teacher_salary = TeacherSalaryForm()
            context = {"form": teacher_salary}
            return render(request, "teachers/add_salary.html", context)
        return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
            salary = Teacher_salary()
            teacher_id = Teacher.objects.get(id=request.POST.get('teacher_id'))
            salary.total_amount = request.POST.get('total_amount')
            salary.status = request.POST.get('status')
            salary.paid_date = request.POST.get('paid_date')
            salary.teacher_id = teacher_id
            salary.save()

            return redirect('salary-teacher')
        return redirect('/login/')


@login_required(login_url='login')
def teachers_salary(request):
    """ Returns the salary of teachers """
    salary_list = Teacher_salary.objects.all()
    context = {"data": salary_list}
    if request.method == "POST":
        search = request.POST.get('search')
        salary = Teacher_salary.objects.filter(teacher_id__first_name__icontains=search)
        context = {"data": salary}
        return render(request, 'teachers/teacher_salary.html', context)
    return render(request, 'teachers/teacher_salary.html', context)


class Subject_add_View(View):
    """ This function adds subjects """

    def get(self, request):
        if request.user.is_authenticated:
            subject = SubjectCreationForm()
            context = {"form": subject}
            return render(request, "subjects/add_subject.html", context)
        return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
            subject = Subject()
            course_code = Course.objects.get(
                id=request.POST.get('course_code'))
            subject.subject_code = request.POST.get('subject_code')
            subject.subject_name = request.POST.get('subject_name')
            subject.semester = request.POST.get('semester')
            subject.credit_hours = request.POST.get('credit_hours')
            subject.course_code = course_code
            subject.save()

            return redirect('index-subject')
        return redirect('/login/')


@login_required(login_url='login')
def subjects_index(request):
    """ Returns the list of subjects """
    subject_list = Subject.objects.all()
    context = {"data": subject_list}
    if request.method == "POST":
        search = request.POST.get('search')
        subjects = Subject.objects.filter(subject_name__icontains=search)
        context = {"data": subjects}
        return render(request, 'subjects/subject_index.html', context)
    return render(request, 'subjects/subject_index.html', context)


class Teacher_assign_subject_View(View):
    """ This function assigns subjects to teachers """

    def get(self, request):
        if request.user.is_authenticated:
            teacher_subject = TeacherSubjectCreationForm()
            context = {"form": teacher_subject}
            return render(request, "teachers/assign_subject.html", context)
        return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
            teacher_subject = Subject_of_teacher()
            course_name = Course.objects.get(
                id=request.POST.get('course_name'))
            teacher_id = Teacher.objects.get(id=request.POST.get('teacher_id'))
            subject_name = Subject.objects.get(
                id=request.POST.get('subject_name'))
            teacher_subject.assign_date = request.POST.get('assign_date')
            teacher_subject.total_classes = request.POST.get('total_classes')
            teacher_subject.course_name = course_name
            teacher_subject.teacher_id = teacher_id
            teacher_subject.subject_name = subject_name
            teacher_id.save()

            return redirect('index-teacher')
        return redirect('/login/')


class Student_fee_View(View):
    """ This function adds record of students fee """

    def get(self, request):
        if request.user.is_authenticated:
            student_fee = StudentFeeForm()
            context = {"form": student_fee}
            return render(request, "students/student_fee.html", context)
        return redirect('/login/')

    def post(self, request):
        if request.user.is_authenticated:
            student_fee = Student_fee()
            roll_no = Student.objects.get(id=request.POST.get('roll_no'))
            student_fee.fee_voucher = request.POST.get('fee_voucher')
            student_fee.amount = request.POST.get('amount')
            student_fee.posting_date = request.POST.get('posting_date')
            student_fee.status = request.POST.get('status')
            student_fee.roll_no = roll_no
            student_fee.save()

            return redirect('fee-index-student')
        return redirect('/login/')


@login_required(login_url='login')
def students_fee_index(request):
    """ Returns the list of students fee """
    fee_list = Student_fee.objects.all()
    context = {"data": fee_list}
    if request.method == "POST":
        search = request.POST.get('search')
        fee = Student_fee.objects.filter(roll_no__first_name__icontains=search)
        context = {"data": fee}
        return render(request, 'students/student_fee_index.html', context)
    return render(request, 'students/student_fee_index.html', context)
