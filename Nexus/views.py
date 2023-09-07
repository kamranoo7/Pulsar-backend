from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer,InstructorSerializer
from .models import Instructor
#Student-View
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


#Instructor-view    
class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer



from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer

#Course-view
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

from rest_framework import viewsets
from .models import Enrollment
from .serializers import EnrollmentSerializer

#Enrollment-view

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer


from .models import Assignment
from.serializers import AssignmentSerializer    
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
#Assignment-view
class AssignmentViewSet(viewsets.ModelViewSet):

    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
     # Ensure the user is authenticated

   
        
from .models import Submission 
from .serializers import SubmissionSerializer


#Submission-view
class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer



from rest_framework import viewsets
from .models import Department
from .serializers import DepartmentSerializer
#Department-view
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer




from rest_framework import viewsets
from .models import Announcement
from .serializers import AnnouncementSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
#Announcement-view
class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    


#Chatbot


#Student_login
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from rest_framework.decorators import api_view

@api_view(['POST'])
def login_student(request):
    if request.method == 'POST':
        email = request.data.get('email')
        name = request.data.get('name')

        try:
            student = Student.objects.get(email=email)
        except Student.DoesNotExist:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Check if the provided name matches the student's name
        if student.name == name:
            # Authentication is successful
            # You can add additional authentication logic here if needed

            # For example, you can check the password, but make sure to have proper security measures in place
            # if student.check_password(password):
            #     return Response({'message': 'Authentication successful'}, status=status.HTTP_200_OK)

            return Response({'message': 'Authentication successful'}, status=status.HTTP_200_OK)

        # If the provided name doesn't match the student's name
        return Response({'message': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)



       

#Instructor_login
from rest_framework.response import Response
from rest_framework import status
from .models import Instructor
from rest_framework.decorators import api_view

@api_view(['POST'])
def instructor_Login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        name = request.data.get('name')

        try:
            instructor = Instructor.objects.get(email=email)
        except Student.DoesNotExist:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        # Check if the provided name matches the student's name
        if instructor.name == name:
            # Authentication is successful
            # You can add additional authentication logic here if needed

            # For example, you can check the password, but make sure to have proper security measures in place
            # if student.check_password(password):
            #     return Response({'message': 'Authentication successful'}, status=status.HTTP_200_OK)

            return Response({'message': 'Authentication successful'}, status=status.HTTP_200_OK)

        # If the provided name doesn't match the student's name
        return Response({'message': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({'message': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)
                

#Ticket System
from .models import Ticket
from .serializers import TicketSerializer
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer



#Chatbot
# views.py
from django.http import HttpResponse

def chatbot_response(request):
    if request.method == 'GET':
        user_input = request.GET.get('user_input', '').lower()
        print(f"Received user_input: {user_input}")

        try:
            response = generate_chatbot_response(user_input)
        except Exception as e:
            print(f"Error: {str(e)}")
            response = "An error occurred while processing your request."

        return HttpResponse(response, content_type='text/plain')

from .models import Student, Course, Assignment

def generate_chatbot_response(user_input):
    response = ""

    if "student" in user_input:
        # Query the database to get all student names
        student_names = Student.objects.values_list('name', flat=True)
        
        if student_names:
            # Join the student names into a comma-separated string
            response = f"Student names: {', '.join(student_names)}"
        else:
            response = "There are no students in the database."
    
    elif "student_name" in user_input:
        # Extract the student name from the user input
        student_name = user_input.split("student_name", 1)[1].strip()

        # Query the database to get the student's details by name
        try:
            student = Student.objects.get(name__iexact=student_name)
            response = f"Student Details:\nName: {student.name}\nStudent ID: {student.student_id}\nGender: {student.gender}\nDate of Birth: {student.date_of_birth}\nMajor: {student.major}\nEmail: {student.email}\nContact Number: {student.contact_number}\nImage URL: {student.imageUrl}"
        except Student.DoesNotExist:
            response = f"No student found with the name '{student_name}' in the database."
    
    elif "courses" in user_input:
        # Query the database to get a list of all available courses
        courses = Course.objects.all()

        if courses:
            course_list = "\n".join([course.course_name for course in courses])
            response = f"Available Courses:\n{course_list}"
        else:
            response = "There are no courses available in the database."
  
    elif "assignment" in user_input:
        # Query the database to get a list of assignment titles
        assignments = Assignment.objects.all()

        if assignments:
            assignment_list = "\n".join([assignment.title for assignment in assignments])
            response = f"Assignment Titles:\n{assignment_list}"
        else:
            response = "There are no assignments available in the database."                
    else:
        response = "I'm sorry, I don't understand your query."

    return response
