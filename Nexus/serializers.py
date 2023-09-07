from rest_framework import serializers
from .models import Student
from .models import Instructor  # Add this import

#Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

#Instructor        
class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = '__all__'
from rest_framework import serializers
from .models import Course

#Course

class CourseSerializer(serializers.ModelSerializer):
    instructor_name = serializers.CharField(source='instructor.name', read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'course_code', 'course_name', 'department', 'credits', 'description','imageUrl', 'instructor', 'instructor_name']
from rest_framework import serializers
from .models import Enrollment

#Enrollment

from rest_framework import serializers
from .models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    course_name = serializers.ReadOnlyField(source='course.course_name')
    student_id=serializers.ReadOnlyField(source="student.student_id")
    class Meta:
        model = Enrollment
        fields = '__all__'
#Assignment
from .models import Assignment
class AssignmentSerializer(serializers.ModelSerializer):
    course_name = serializers.StringRelatedField(source='course', read_only=True)
    instructor_name = serializers.StringRelatedField(source='name', read_only=True)

    class Meta:
        model = Assignment
        fields = '__all__'

from .models import Submission
#Submission
class SubmissionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Submission
        fields = "__all__"

#Department
from .models import Department
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

#Announcement

from rest_framework import serializers
from .models import Announcement

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'







from rest_framework import serializers
from .models import Ticket


#Ticket
class TicketSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Ticket
        fields = '__all__'
