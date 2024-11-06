from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('signup/',views.signup , name='signup'),
    path('login/',views.login_user ,name='login'),
    path('message/<str:title>/<str:message>/',views.message, name='message'),
    path('logout/',views.logout,name='logout')


]