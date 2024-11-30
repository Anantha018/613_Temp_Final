# Forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Course, Discussion, Inbox

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'thumbnail']

class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label="I am a")
    email = forms.EmailField(required=True, label="Email Address")  # Add the email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']  # Include email here

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Save the email
        if commit:
            user.save()
        return user


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['course', 'title', 'content']

class InboxForm(forms.ModelForm):
    class Meta:
        model = Inbox
        fields = ['to', 'subject', 'message']
