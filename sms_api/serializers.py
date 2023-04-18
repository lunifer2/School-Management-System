from rest_framework import serializers
from SMS.models import Course, Teacher_salary, Teacher_salary_allowance, Subject_of_teacher, Teacher, Subject, Student, Course_of_student, Student_fee
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields =('id',
                 'email',
                 'username',
                 'password')
        extra_kwargs = {
            'password':{"write_only": True},
        }
        
    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password1')
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return user
       

        return super().create(validated_data)   

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'username',
                  'password')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id',
                  'course_code',
                  'course_name',
                  'semester_or_year',
                  'no_of_year')


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id',
                  'subject_code',
                  'subject_name',
                  'semester',
                  'credit_hours',
                  'course_code')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'roll_no', 'first_name',
                  'last_name',
                  'middle_name',
                  'father_name',
                  'mobile_no',
                  'course_name',
                  'session',
                  'applicant_status',
                  'application_status',
                  'dob',
                  'gender',
                  'address',
                  'admission_date',
                  'email')


class Course_of_studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_of_student
        fields = ('id',
                  'course_code',
                  'subject_code',
                  'roll_no',
                  'assign_date')


class Student_feeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_fee
        fields = ('id',
                  'fee_voucher',
                  'roll_no',
                  'amount',
                  'posting_date',
                  'status')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'mobile_no',
                  'course_name',
                  'session',
                  'teacher_status',
                  'application_status',
                  'dob',
                  'gender',
                  'address',
                  'hire_date',
                  'email')


class Subject_of_teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject_of_teacher
        fields = ('id',
                  'course_name',
                  'teacher_id',
                  'subject_name',
                  'assign_date',
                  'total_classes')


class Teacher_salary_allowanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher_salary_allowance
        fields = ('id',
                  'teacher_id',
                  'basic_salary',
                  'medical_allowance')


class Teacher_salarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher_salary
        fields = ('id',
                  'teacher_id',
                  'total_amount',
                  'status',
                  'paid_date')
