from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, InstructorViewSet,CourseViewSet,EnrollmentViewSet,AssignmentViewSet,SubmissionViewSet,DepartmentViewSet,AnnouncementViewSet,TicketViewSet

# Create a router and register the StudentViewSet
router = DefaultRouter()
#Student
router.register(r'students', StudentViewSet)
#submission
router.register(r'submissions', SubmissionViewSet)
#Department
router.register(r'departments', DepartmentViewSet)
#instructorsac
router.register(r'instructors', InstructorViewSet)
#courses
router.register(r'courses', CourseViewSet)
#Enrollments
router.register(r'enrollments', EnrollmentViewSet)
#Assignments
router.register(r'assignments', AssignmentViewSet)
#Announcements
router.register(r'announcements', AnnouncementViewSet)
router.register(r'ticket',TicketViewSet)
from django.urls import path
from . import views
urlpatterns = [
    # Include the API URLs from the router
    path('api/', include(router.urls)),
    path('login/', views.login_student, name='login_student'),
    path('loginn/', views.instructor_Login, name='instructor_Login'),
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'), 
]
