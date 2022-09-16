from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', admin.site.urls),
    path('signup/', admin.site.urls),
    path('question/$<id>', admin.site.urls),
    path('ask/', admin.site.urls),
    path('popular/', admin.site.urls),
    path('new/', admin.site.urls),
]
