from django import forms
from rateMyUogCourse.models import WebsiteFeedback
from student.models import Student
from django.contrib.auth.models import User

class WebsiteFeedback(forms.ModelForm):
    class Meta:
        model = WebsiteFeedback
        exclude = ['feedbackTime']

class StudentRegistrationForm(forms.ModelForm):
    # guid = forms.CharField(max_length=7, )
    email = forms.EmailField(max_length=100, help_text = "Email Address")
    name = forms.CharField(max_length=200, help_text = "Name")
    password = forms.CharField(widget=forms.PasswordInput(), help_text = "Password")
    programType = forms.CharField(max_length=4, help_text = "Program Type")
    # user = User.objects.create(username = email, password = password)

    class Meta:
        model = Student
        fields = ('name', 'email', 'password', 'programType',)
        
    # def save(self, commit=True):
        
        # student = super(StudentRegistrationForm, self).save(commit=False)
        

        # user = User.objects.create_user(
            # username=self.cleaned_data['email'],
            # email=self.cleaned_data['email'],
            # password=self.cleaned_data['password']
        # )

        # student.user = user

        # if commit:
            # student.save()
        # return student
