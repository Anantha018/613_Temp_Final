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


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'thumbnail']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['thumbnail'].widget = forms.ClearableFileInput(attrs={'class': 'custom-file-input'})
        self.fields['thumbnail'].widget.clear_checkbox_label = None  # Hide the clear checkbox


class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'thumbnail']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the thumbnail field to remove the "Clear" checkbox
        self.fields['thumbnail'].widget = forms.ClearableFileInput(attrs={'class': 'custom-file-input'})
        self.fields['thumbnail'].widget.can_clear = False  # Disable the "Clear" checkbox
        

class MessageForm(forms.Form):
    recipient = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="To",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    subject = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['course', 'title', 'content']

class InboxForm(forms.ModelForm):
    class Meta:
        model = Inbox
        fields = ['to', 'subject', 'message']
