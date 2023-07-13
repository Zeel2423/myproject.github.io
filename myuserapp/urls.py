from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('homepageview',views.home,name='home'),

    path('home',views.home),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('teachers',views.teachers,name="teachers"),
    path('pricing',views.pricing,name="pricing"),
    path('login',views.login,name='login'),
    path('loginpageprocess',views.loginpageprocess,name='loginpageprocess'),
    path('userhome',views.userhome,name='userhome'),

    path('userlogout',views.userlogout,name='userlogout'),
    
    path('changepassword',views.changepassword,name='changepassword'),
    path('changepasswordprocess',views.changepasswordprocess,name='changepasswordprocess'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword'),
    path('forgotpasswordprocess',views.forgotpasswordprocess,name='forgotpasswordprocess'),
    path('signup',views.signup,name='signup'),
    path('signup_addprocess',views.signup_addprocess,name='signup_addprocess'),
    path('mailsenddemo',views.mailsenddemo,name='mailsenddemo'),
    path('fees',views.fees,name='fees'),
    path('timetable',views.timetable,name='timetable'),
    path('reportcard',views.reportcard,name='reportcard'),



]