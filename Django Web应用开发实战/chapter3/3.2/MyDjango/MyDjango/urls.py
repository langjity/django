"""MyDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
urlpatterns = [
    # 指向内置admin系统的路由文件sites.py
    path('admin/', admin.site.urls),
    # 指向index的路由文件urls.py
    path('', include(('index.urls', 'index'), namespace='index')),
    # 指向user的路由文件urls.py
    path('user/', include(('user.urls', 'user'), namespace='user'))
]
