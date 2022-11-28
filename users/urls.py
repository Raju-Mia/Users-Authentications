from django.urls import path
from . import views as user_views

urlpatterns = [
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('customregister/', user_views.customregister, name='customregister'),

    path('login/', user_views.login_form, name='login'),
    path('logout/', user_views.logout_form, name='logout'),

    #password
    path('passwordchange/', user_views.passwordchange, name='passwordchange'),

    #password change without old password
    path('passwordchangeop/', user_views.passwordchangeop, name='passwordchangeop'),
]
