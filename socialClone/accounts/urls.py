from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns=[
    path('signup', views.signup.as_view(), name='signupPage'),
    path('login', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='loginPage'),
    path('logout', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logoutPage'),
]


# from django.conf import settings
# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns
