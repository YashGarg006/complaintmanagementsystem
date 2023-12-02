from django.urls import include, path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('',views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('signin/',auth_views.LoginView.as_view(template_name='CMsystem/signin.html'), name='signin'),
    path('logout/', auth_views.LogoutView.as_view(template_name='CMsystem/logout.html'), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('counter/', views.counter, name='counter'),
    # forgot passowrd url's
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='CMsystem/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset-done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='CMsystem/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='CMsystem/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='CMsystem/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    # forgot password url's ended

    # reset password url 
    path('password/', views.change_password, name='change_password'),

    # add complain path
    path('complaints/', views.complaints, name='complaints'),

    # unsolved complains on user side url
    path('list/',views.list,name='list'),

    #solved complaints urls 
    path('slist/',views.slist,),
    
    path('login_redirect/',views.login_redirect,name='login_redirect'),

    path('passwords/', views.change_password_g, name='change_password_g'),
    # all complaints in supervisor
    path('allcomplaints/', views.allcomplaints, name='allcomplaints'),
    # solved complaints in supervisor
    path('solved/', views.solved, name='solved'),

    # supervisor complaint pdf detail viewer
    path('pdf_g/',views.pdf_viewer,name='view'),
    # student complaint pdf detail viewer
    path('pdf/',views.pdf_view,name='view'),
]