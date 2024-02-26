from django.urls import path
from rateMyUogCourse import views


app_name = 'rateMyUogCourse'

urlpatterns = [
path('login/', views.login, name='login'),
path('signup/', views.signup, name='signup'),
path('feedback/', views.feedback, name='feedback'),
path('searchCourses/<str:course_name>/<str:program_type>', views.search, name = 'search')
]
