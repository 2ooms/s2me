"""s2me URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

from frontend import views as frontend_view
from contact import views as contact_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', frontend_view.home, name='home'),
    url(r'^frontend/', frontend_view.frontend, name='frontend'),
    url(r'^backend/', frontend_view.backend, name='backend'),
    url(r'^backend/battleship', frontend_view.backend_battleship, name='backend_battleship'),
    url(r'^about/', frontend_view.about, name='about'),
    url(r'^contact/', contact_view.contact, name='contact'),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)