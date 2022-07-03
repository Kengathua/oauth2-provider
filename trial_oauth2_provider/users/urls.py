from django.urls import path, include, re_path
from trial_oauth2_provider.users import views


urlpatterns = [
    path('sign-in/',views.loginPage, name='sign-in'),
    path('logout/',views.logoutUser, name='logout'),
]

urlpatterns = [
    re_path(r'^profile/$', views.profile),
]
