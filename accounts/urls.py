from django.urls import path

from accounts.views import login_view, logout_view, registration_view

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('registration/', registration_view, name='registration'),
]