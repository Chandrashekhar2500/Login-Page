from django.contrib import admin
from django.urls import path,include
from . views import hello,SignUpView

from django.views.generic.base import TemplateView 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUpView),
    path('hello/', hello),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    
]