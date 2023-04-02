from django.urls import path
from . import views
from django.views.generic import TemplateView






urlpatterns = [
    path('multiemail_static/',views.static,name='home'),
    path('multiemail_dynamic/',views.dynamic,name='d'),
    path('', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),

    
    ]