"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from news.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name = 'home' ),
    path('create_category/', createCategory, name='create_category'),
    path('user_register/',user_register, name='create_user'),
    path('news/create/',createNew,name='create_news'),

    path('detail/<int:id>/',detail,name='detail'),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit/<int:id>/', editnews, name= 'edit'),
    path('logout/',Logout,name = "logout"),
    path('login/', Login, name = "login"),
    
    #path('login')

    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

