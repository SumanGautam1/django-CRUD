"""
URL configuration for myProject project.

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
from django.contrib import admin
from django.urls import path
from myApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', details, name='details'),
    path('delete/<int:id>', delete_data, name='delete'),
    path('edit/<int:id>', edit_data, name='edit'),
    path('bin/', recycle, name='bin'),
    path('deletebin/<int:id>', delete_bin, name='deletebin'),
    path('restorebin/<int:id>', restore_bin, name='restorebin'),
    path('clearbin/', clearbin, name='clearbin')
]
