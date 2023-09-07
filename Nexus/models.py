from django.db import models
#Entity -7
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    class Meta:
        managed = False

#Entity-1

class Student(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    MAJOR_CHOICES = [
        ('Computer Science', 'Computer Science'),
        ('Engineering', 'Engineering'),
        ('Business', 'Business'),
        # Add other majors here
    ]

    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    major = models.CharField(max_length=50, choices=MAJOR_CHOICES)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    imageUrl = models.URLField(blank=True)

    def __str__(self):
        return self.name
    


#Entity-2    
class Instructor(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    DEPARTMENT_CHOICES = [
        ('Science', 'Science'),
        ('Arts', 'Arts'),
        ('Engineering', 'Engineering'),
        # Add other departments here
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    imageUrl = models.URLField(blank=True)
    def __str__(self):
        return self.name
#Entity-3    
from django.db import models
from Nexus.models import Instructor  # Import the Instructor model
from django.db import models
from Nexus.models import Instructor  # Import the Instructor model
from Nexus.models import Department  # Import the Department model

class Course(models.Model):
    DEPARTMENT_CHOICES = [
        ('Science', 'Science'),
        ('Arts', 'Arts'),
        ('Engineering', 'Engineering'),
        # Add other departments here
    ]
    imageUrl = models.URLField(blank=True)
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    credits = models.PositiveIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.course_name


#Entity-4    
from django.db import models
from Nexus.models import Student  # Import the Student model
from Nexus.models import Course  # Import the Course model

from django.db import models
from .models import Student, Course

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.name} - {self.course.course_name}"


#Entity-5
class Assignment(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE,related_name='assignments')
    name = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
##Entity-6    
class Submission(models.Model):
    STATUS_CHOICES = [
        ('Submitted', 'Submitted'),
        ('Late', 'Late'),
        ('Graded', 'Graded'),
    ]

    submission_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    remarks = models.TextField()
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.assignment.title} - {self.student.name}"
    
#Entity-7

#Entity-8
from django.db import models
from Nexus.models import Department, Course, Instructor

class Announcement(models.Model):
    DEPARTMENT_CHOICES = [
        ('Science', 'Science'),
        ('Arts', 'Arts'),
        ('Engineering', 'Engineering'),
        # Add other departments here
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    publish_date = models.DateField()
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



#Ticket system

    


from django.db import models
from Nexus.models import Student  # Import the Student model

class Ticket(models.Model):
    TICKET_TYPES = [
        ('Attendance', 'Attendance'),
        ('Withdrawal', 'Withdrawal'),
        ('Assignment Evaluation', 'Assignment Evaluation'),
        # Add more ticket types as needed
    ]

    status = models.CharField(max_length=20, default='Open')
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ticket_type = models.CharField(max_length=200, choices=TICKET_TYPES)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticket_type} - {self.student.name}"
