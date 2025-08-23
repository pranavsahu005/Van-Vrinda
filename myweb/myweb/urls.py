from .views import *
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
from master.urls import producturls

urlpatterns = [
    path('master/', include(producturls),name='master'),
    path('front', front, name='front'),
    path('homepage', homepage, name='homepage'),
    path('signin', signin, name='signin'),
    path('signup', signup, name='signup'),
    
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
