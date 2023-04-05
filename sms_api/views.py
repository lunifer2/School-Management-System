from django.shortcuts import render
from .serializers import CourseSerializer, SubjectSerializer, StudentSerializer, Course_of_studentSerializer, Teacher_salary_allowanceSerializer, Teacher_salarySerializer, TeacherSerializer, Subject_of_teacherSerializer, Student_feeSerializer
from SMS.models import Course, Teacher, Subject, Student, Course_of_student, Student_fee, Subject_of_teacher, Teacher_salary, Teacher_salary_allowance
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView

# Create your views here.


class CustomResponse():
    """ This class helps to inherit responses"""

    def successResponse(self, code, msg, data=dict()):
        context = {
            "status_code": code,
            "message": msg,
            "data": data,
            "error": []
        }
        return context

    def errorResponse(self, status_code, msg, error=dict()):
        res = {
            "status_code": status_code,
            "message": msg,
            "data": [],
            "error": error
        }
        return res


class CourseApiView(APIView):
    """ This class adds and shows the list of courses"""

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        response = CustomResponse()
        return Response(response.successResponse(200, "Course List", serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        response = CustomResponse()
        if serializer.is_valid():
            serializer.save()
            return Response(response.successResponse(200, "Course Added successfully", serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(response.errorResponse(408, "Validation Error", serializer.errors), status=status.HTTP_408_REQUEST_TIMEOUT)


class CourseApiIdView(APIView):
    """ This class adds and shows the list of courses by id """

    def get_object(self, id):
        try:
            data = Course.objects.get(id=id)
            return data
        except Course.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"msg": "Deleted successfully"}, status=status.HTTP_200_OK)


class SubjectApiView(APIView):
    """ This class adds and shows the list of subjects"""

    def get(self, request):
        subject = Subject.objects.all()
        serializer = SubjectSerializer(subject, many=True)
        response = CustomResponse()
        return Response(response.successResponse(200, "Subject List", serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        response = CustomResponse()
        if serializer.is_valid():
            serializer.save()
            return Response(response.successResponse(200, "Subject Added successfully", serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(response.errorResponse(408, "Validation Error", serializer.errors), status=status.HTTP_408_REQUEST_TIMEOUT)


class SubjectApiIdView(APIView):
    """ This class adds and shows the list of courses by id """

    def get_object(self, id):
        try:
            data = Subject.objects.get(id=id)
            return data
        except Subject.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubjectSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SubjectSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"msg": "Deleted successfully"}, status=status.HTTP_200_OK)


class StudentApiView(APIView):
    """ This class adds and shows the list of students """

    def get(self, request):
        subject = Student.objects.all()
        serializer = StudentSerializer(subject, many=True)
        response = CustomResponse()
        return Response(response.successResponse(200, "Student List", serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        response = CustomResponse()
        if serializer.is_valid():
            serializer.save()
            return Response(response.successResponse(200, "Student Added successfully", serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(response.errorResponse(408, "Validation Error", serializer.errors), status=status.HTTP_408_REQUEST_TIMEOUT)


class StudentApiIdView(APIView):
    """ This class adds and shows the list of students by id """

    def get_object(self, id):
        try:
            data = Student.objects.get(id=id)
            return data
        except Student.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"msg": "Deleted successfully"}, status=status.HTTP_200_OK)


class CourseOfStudentApiView(APIView):
    """ This class adds and shows the list of courses of students """

    def get(self, request):
        courseOfStudent = Course_of_student.objects.all()
        serializer = Course_of_studentSerializer(courseOfStudent, many=True)
        response = CustomResponse()
        return Response(response.successResponse(200, "Course of Student List", serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Course_of_studentSerializer(data=request.data)
        response = CustomResponse()
        if serializer.is_valid():
            serializer.save()
            return Response(response.successResponse(200, "Course of Student Added successfully", serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(response.errorResponse(408, "Validation Error", serializer.errors), status=status.HTTP_408_REQUEST_TIMEOUT)


class CourseOfStudentApiIdView(APIView):
    """ This class adds and shows the list of courses of students by id"""

    def get_object(self, id):
        try:
            data = Course_of_student.objects.get(id=id)
            return data
        except Course_of_student.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Course_of_studentSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Course_of_studentSerializer(
            data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"msg": "Deleted successfully"}, status=status.HTTP_200_OK)


class TeacherSalaryApiView(APIView):
    """ This class adds and shows the list of salary of teachers """

    def get(self, request):
        teacher_salary = Teacher_salary.objects.all()
        serializer = Teacher_salarySerializer(teacher_salary, many=True)
        response = CustomResponse()
        return Response(response.successResponse(200, "Teacher's Salary List", serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Teacher_salarySerializer(data=request.data)
        response = CustomResponse()
        if serializer.is_valid():
            serializer.save()
            return Response(response.successResponse(200, "Salary of Teacher Added successfully", serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(response.errorResponse(408, "Validation Error", serializer.errors), status=status.HTTP_408_REQUEST_TIMEOUT)


class TeacherSalaryApiIdView(APIView):
    """ This class adds and shows the list of salary of teachers by id """

    def get_object(self, id):
        try:
            data = Teacher_salary.objects.get(id=id)
            return data
        except Teacher_salary.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Teacher_salarySerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Teacher_salarySerializer(
            data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"msg": "Deleted successfully"}, status=status.HTTP_200_OK)


class TeacherSalaryAllowanceApiView(APIView):
    """ This class adds and shows the list of salary allowance of teachers """

    def get(self, request):
        teacher_salary_allowance = Teacher_salary_allowance.objects.all()
        serializer = Teacher_salary_allowanceSerializer(
            teacher_salary_allowance, many=True)
        response = CustomResponse()
        return Response(response.successResponse(200, "Teacher's Salary Allowance List", serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Teacher_salary_allowanceSerializer(data=request.data)
        response = CustomResponse()
        if serializer.is_valid():
            serializer.save()
            return Response(response.successResponse(200, "Salary alowance of Teacher Added successfully", serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(response.errorResponse(408, "Validation Error", serializer.errors), status=status.HTTP_408_REQUEST_TIMEOUT)


class TeacherSalaryAllowanceApiIdView(APIView):
    """ This class adds and shows the list of salary allowance of teachers by id """

    def get_object(self, id):
        try:
            data = Teacher_salary_allowance.objects.get(id=id)
            return data
        except Teacher_salary_allowance.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Teacher_salary_allowanceSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Teacher_salary_allowanceSerializer(
            data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"msg": "Deleted successfully"}, status=status.HTTP_200_OK)


class TeacherApiView(APIView):
    """ This class adds and shows the list of teachers """

    def get(self, request):
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        response = CustomResponse()
        return Response(response.successResponse(200, "Teacher List", serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        response = CustomResponse()
        if serializer.is_valid():
            serializer.save()
            return Response(response.successResponse(200, "Teacher Added successfully", serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(response.errorResponse(408, "Validation Error", serializer.errors), status=status.HTTP_408_REQUEST_TIMEOUT)


class TeacherApiIdView(APIView):
    """ This class adds and shows the list ofteachers by id """

    def get_object(self, id):
        try:
            data = Teacher.objects.get(id=id)
            return data
        except Teacher.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TeacherSerializer(data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"msg": "Deleted successfully"}, status=status.HTTP_200_OK)


class SubjectOfTeacherApiView(APIView):
    """ This class adds and shows the list of subject of teachers """

    def get(self, request):
        subject_of_teacher = Subject_of_teacher.objects.all()
        serializer = Subject_of_teacherSerializer(
            subject_of_teacher, many=True)
        response = CustomResponse()
        return Response(response.successResponse(200, "Teacher's Subject List", serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Subject_of_teacherSerializer(data=request.data)
        response = CustomResponse()
        if serializer.is_valid():
            serializer.save()
            return Response(response.successResponse(200, "Subject of Teacher Added successfully", serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(response.errorResponse(408, "Validation Error", serializer.errors), status=status.HTTP_408_REQUEST_TIMEOUT)


class SubjectOfTeacherApiIdView(APIView):
    """ This class adds and shows the list of subject of teachers by id """

    def get_object(self, id):
        try:
            data = Subject_of_teacher.objects.get(id=id)
            return data
        except Subject_of_teacher.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Subject_of_teacherSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Subject_of_teacherSerializer(
            data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"msg": "Deleted successfully"}, status=status.HTTP_200_OK)


class StudentFeeApiView(APIView):
    """ This class adds and shows the list of student's fee """

    def get(self, request):
        subject_fee = Student_fee.objects.all()
        serializer = Student_feeSerializer(subject_fee, many=True)
        response = CustomResponse()
        return Response(response.successResponse(200, "Student Fee List", serializer.data), status=status.HTTP_200_OK)

    def post(self, request):
        serializer = Student_feeSerializer(data=request.data)
        response = CustomResponse()
        if serializer.is_valid():
            serializer.save()
            return Response(response.successResponse(200, "Student fee Added successfully", serializer.data), status=status.HTTP_200_OK)
        else:
            return Response(response.errorResponse(408, "Validation Error", serializer.errors), status=status.HTTP_408_REQUEST_TIMEOUT)


class StudentFeeApiIdView(APIView):
    """ This class adds and shows the list of student's fee id"""

    def get_object(self, id):
        try:
            data = Student_fee.objects.get(id=id)
            return data
        except Student_fee.DoesNotExist:
            return None

    def get(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Student_feeSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = Student_feeSerializer(
            data=request.data, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        instance = self.get_object(id)

        if not instance:
            return Response({"msg": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

        instance.delete()
        return Response({"msg": "Deleted successfully"}, status=status.HTTP_200_OK)