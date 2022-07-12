"""alpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from django.views.generic import RedirectView
from catalogue.views import loginPage, logoutUser, registerPage, homePage, profile, update
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordChangeView
from catalogue import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage,name='home'),
    path('catalogue/',include('catalogue.urls')),
    path('signup/',registerPage,name='signup'),
    path('login/',loginPage, name='login'),
    path('logout/',logoutUser, name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/edit_profile/', update, name='edit_profile'),
    path('accounts/password_change', views.PasswordsChangeView.as_view(template_name='registration/password_change.html'),name='password_change'),
    path('password_success', views.password_success, name='password_success'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)