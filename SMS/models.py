from django.db import models

# Create your models here.


class Course(models.Model):
    course_code = models.IntegerField()
    course_name = models.CharField(max_length=250)
    semester_or_year = models.CharField(max_length=250)
    no_of_year = models.CharField(max_length=250)

    def __str__(self):
        return self.course_name

    class Meta:
        db_table = "course"


class Subject(models.Model):
    subject_code = models.IntegerField()
    subject_name = models.CharField(max_length=250)
    semester = models.IntegerField()
    credit_hours = models.IntegerField()
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name

    class Meta:
        db_table = "subject"


class Student(models.Model):
    roll_no = models.IntegerField()
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250)
    father_name = models.CharField(max_length=250, blank=True)
    mobile_no = models.IntegerField()
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.CharField(max_length=250)
    applicant_status = models.CharField(max_length=100)
    application_status = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    admission_date = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "student_info"


class Course_of_student(models.Model):
    course_code = models.ForeignKey(Course, on_delete=models.CASCADE)
    subject_code = models.ForeignKey(Subject, on_delete=models.CASCADE)
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    assign_date = models.DateField()

    def __date__(self):
        return self.assign_date

    class Meta:
        db_table = "student_course"


class Student_fee(models.Model):
    fee_voucher = models.IntegerField()
    roll_no = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.FloatField(max_length=100)
    posting_date = models.DateTimeField()
    status = models.CharField(max_length=250)

    def __date__(self):
        return self.posting_date

    class Meta:
        db_table = "student_fee"


class Teacher(models.Model):
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, blank=True)
    last_name = models.CharField(max_length=250)
    mobile_no = models.IntegerField()
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.CharField(max_length=250)
    teacher_status = models.CharField(max_length=100)
    application_status = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    hire_date = models.DateField()
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "teacher_info"


class Subject_of_teacher(models.Model):
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assign_date = models.DateField()
    total_classes = models.IntegerField()

    def __date__(self):
        return self.assign_date

    class Meta:
        db_table = "teacher_subject"


class Teacher_salary_allowance(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    basic_salary = models.FloatField()
    medical_allowance = models.FloatField()

    def __float__(self):
        return self.basic_salary

    class Meta:
        db_table = "teacher_salary_allowance"


class Teacher_salary(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    total_amount = models.FloatField()
    status = models.CharField(max_length=250)
    paid_date = models.DateTimeField()

    def __str__(self):
        return self.status

    class Meta:
        db_table = "teacher_salary"
