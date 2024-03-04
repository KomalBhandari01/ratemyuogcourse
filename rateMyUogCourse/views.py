from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from rateMyUogCourse.models import CourseSearchTable

from lecturer.models import Course
from rateMyUogCourse.forms import WebsiteFeedback, StudentRegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse


def mainPage(request):
 return render(request, 'rateMyUogCourse/homepage.html')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(username = email, password = password)
        print(user)
        
        if user is not None:
            login(request, user)
            return redirect(reverse(mainPage))
        else:
            return HttpResponse("Invalid login details.")
            
    return render(request, 'rateMyUogCourse/login.html')

def signup(request):

    # registered = False
    
    if request.method == 'POST':
    
        registration_form = StudentRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            
            student = registration_form.save(commit=False)

            user = User.objects.create_user(
                username=registration_form.cleaned_data['email'],
                email=registration_form.cleaned_data['email'],
                password=registration_form.cleaned_data['password']
            )

            student.user = user

            # not sure about how to confirm password
            student.guid = student.email.split("@")[0]
            student.user.set_password(student.password)
            student.save()
            return redirect(mainPage)
        else:
            print(registration_form.errors)
        
    else:
        registration_form = StudentRegistrationForm()
    return render(request, 'rateMyUogCourse/signup.html')
 


def feedback(request):
 return render(request, 'rateMyUogCourse/feedbackPage.html')


def search(request, course_name, program_type):

    context_dict={}
    search_results = None

    if(course_name == 'None' and program_type == 'None'):
        search_results =  CourseSearchTable.objects.all()

    else:
 
        try:
            if program_type != 'None':
                course_of_program_type = Course.objects.filter(programType = program_type)
                course_name = [course.courseName for course in course_of_program_type]
                if course_name != 'None':
                    search_results = CourseSearchTable.objects.filter(courseName__in = course_name)

                else:
                    search_results = course_of_program_type
            else:
                search_results = CourseSearchTable.objects.filter(courseName=course_name )
            
        except:
            pass

    context_dict['search_results'] = search_results

    return  render(request, 'rateMyUogCourse/course_rating_overview.html', context=context_dict)

#For testing base.html
def basePage(request):
    return render(request,'base.html')


def save_website_feedback(request):
    if request.method == 'POST':
        form = WebsiteFeedback(request.POST)
        if form.is_valid():
            form.save()

    print('Website feedback saved successfully.')


   


