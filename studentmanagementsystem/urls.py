"""studentmanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from studentmanagementapp import views , HodViews
from studentmanagementsystem import settings

urlpatterns = [
    path('demo',views.ShowDemo),
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage),
    path('doLogin',views.doLogin),
    path('get_user_details',views.GetUserDetails),
    path('logout_user',views.LogoutUser),
    path('admin_home', HodViews.admin_home),
    path('add_staff',HodViews.add_staff),
    path('add_staff_save',HodViews.add_staff_save),
    path('add_courses',HodViews.add_courses),
    path('add_courses_save',HodViews.add_courses_save),
    path('add_student',HodViews.add_student),
    path('add_student_save',HodViews.add_student_save),
    path('add_subject',HodViews.add_subject),
    path('add_subject_save',HodViews.add_subject_save),
    path('manage_staff',HodViews.manage_staff),
    path('manage_student',HodViews.manage_student),
    path('manage_course',HodViews.manage_course),
    path('manage_subject',HodViews.manage_subject),
    


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
