# classnest_Base/models.py
from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, label="I am a")
    email = forms.EmailField(required=True, label="Email Address")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'user_type']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructed_courses')
    students = models.ManyToManyField(User, related_name='enrolled_courses', blank=True)
    thumbnail = models.ImageField(
        upload_to='course_thumbnails/',
        blank=True,
        null=True,
        default='course_thumbnails/default-thumbnail.jpg'
    )

    def __str__(self):
        return self.title


class Profile(models.Model):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    github_link = models.URLField(max_length=200, blank=True, null=True)
    linkedin_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.user_type}"


class Module(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Recording(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  # Add title field
    url = models.URLField()  # Use URLField for recording links

class Assignment(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  # Add title field
    file = models.FileField(upload_to='assignments/')

class Material(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  # Add title field
    file = models.FileField(upload_to='materials/')

class Discussion(models.Model):
    course = models.CharField(max_length=200)
    title = models.TextField()
    content = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is created

    def __str__(self):
        return self.title
    

class Inbox(models.Model):
    to = models.CharField(max_length=200)
    subject = models.TextField()
    message = models.TextField()
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is created

    def __str__(self):
        return self.title
    
    
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    is_read = models.BooleanField(default=False)  # Track if the message is read
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically set the time of creation

    def __str__(self):
        return f"From {self.sender} to {self.receiver}: {self.subject}"