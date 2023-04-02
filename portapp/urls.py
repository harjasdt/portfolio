from django.urls import path
from . import views
from django.views.generic import TemplateView






urlpatterns = [
    path('use/',views.all,name='home'),
    path('', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'api_schema'}
        ), name='swagger-ui'),

    
    ]