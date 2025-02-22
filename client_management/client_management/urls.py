"""
URL configuration for client_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
"""from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clients.urls')),  # Include the clients app URLs
]
"""

"""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clients.urls')),  # Include the clients app URLs (with the api prefix)
]"""

# client_management/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Create a simple view for the root path
def home_view(request):
    return HttpResponse("Welcome to the Client Management API!")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clients.urls')),
    path('', home_view),  # Add this line for the root URL
]

