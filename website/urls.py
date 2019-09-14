from django.urls import path
from . import views


app_name = 'website'

# urlpatterns contains the URL routing list
urlpatterns = [
    # GET /
    path('', views.index, name='index'),
]
