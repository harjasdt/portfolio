from django.urls import path
from . import views
from django.views.generic import TemplateView






urlpatterns = [
    path('clear/',views.team,name='team'),
    path('home/',views.home,name='home'),
    path('goodhome/',views.goodhome,name='goodhome'),
     path('getting/',views.getting,name='getting'),

    path('test/',views.test,name='test'),
    # path('multiemail_static/',views.static,name='home'),
    # path('multiemail_dynamic/',views.dynamic,name='d'),
    # path('', TemplateView.as_view(
    #     template_name='docs.html',
    #     extra_context={'schema_url':'api_schema'}
    #     ), name='swagger-ui'),

    
    ]