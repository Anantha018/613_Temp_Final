from django.contrib import admin
from .models import *

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'thumbnail')

admin.site.register(Course, CourseAdmin)

admin.site.register(Module)
admin.site.register(Recording)
admin.site.register(Assignment)
admin.site.register(Material)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'github_link', 'linkedin_link')
    


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'subject', 'is_read', 'timestamp')
    list_filter = ('is_read', 'timestamp')
    search_fields = ('subject', 'sender__username', 'receiver__username')
    ordering = ('-timestamp',)
    readonly_fields = ('timestamp',)