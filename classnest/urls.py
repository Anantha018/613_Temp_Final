from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('notanadmin/', admin.site.urls),
    path('', include('classnest_Base.urls')),
]
