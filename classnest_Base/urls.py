# classnest_Base/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import viewss
from django.conf import settings
from django.conf.urls.static import static
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', CustomLoginView.as_view(template_name='classnest_Base/login.html'), name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('create-course/', views.create_course_view, name='create-course'),
    path('courses/', views.courses_view, name='courses'),
    path('search-courses/', views.search_courses_view, name='search-courses'),
    
    
    path('course/<int:course_id>/', views.course_detail_view, name='course-detail'),
    
    path('course/delete/<int:course_id>/', views.delete_course_view, name='delete-course'),
    path('course/<int:course_id>/add-module/', views.add_module_view, name='add-module'),
    path('course/<int:course_id>/save-module/', views.save_module_view, name='save-module'),
    
    path('module/<int:module_id>/', views.module_detail_view, name='module-detail'),
    path('module/<int:module_id>/add-recording/', views.add_recording_view, name='add-recording'),
    path('module/<int:module_id>/add-assignment/', views.add_assignment_view, name='add-assignment'),
    path('module/<int:module_id>/add-material/', views.add_material_view, name='add-material'),
    
    path('discussions/', views.discussions_view, name='discussions'),
    path('discussions/<int:discussion_id>/', views.discussion_detail, name='discussion-detail'),
    path('course/<int:course_id>/discussions/', views.discussion_list_view, name='discussion-list'),
    path('course/<int:course_id>/discussions/create/', views.create_discussion, name='create-discussion'),
    path('discussions/<int:discussion_id>/delete/', views.delete_discussion, name='delete-discussion'),

    path('send-message/', views.send_message_view, name='send-message'),
    path('inbox/', views.inbox_view, name='inbox'),
    path('message/<int:message_id>/', views.message_detail_view, name='message-detail'),
    
    path('recording/<int:recording_id>/delete/', views.delete_recording_view, name='delete-recording'),
    path('assignment/<int:assignment_id>/delete/', views.delete_assignment_view, name='delete-assignment'),
    path('material/<int:material_id>/delete/', views.delete_material_view, name='delete-material'),
    
    path('module/<int:module_id>/delete/', views.delete_module_view, name='delete-module'),
    
    path('course/<int:course_id>/edit/', views.edit_course_view, name='edit-course'),
    
    path('instructor/<int:instructor_id>/', views.instructor_detail_view, name='instructor-detail'),
    path('course/<int:course_id>/enrolled-students/', views.enrolled_students_view, name='enrolled-students'),
    path('user/<int:user_id>/', views.user_profile_view, name='user-profile'),
    
    path('profile/', views.profile_view, name='profile'),
    
    path('login/', CustomLoginView.as_view(template_name='classnest_Base/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='classnest_Base/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='classnest_Base/password_change_done.html'), name='password_change_done'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
