"""
URL configuration for snake2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# snake2/urls.py

from django.contrib import admin
from django.urls import path
from firebase_test.views import test_firebase, home  # Import both views here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test-firebase/', test_firebase, name='test_firebase'),  # URL for Firebase test view
    path('', home, name='home'),  # URL for the home view
]
