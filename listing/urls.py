from django.urls import path

from . import views
# Add URLs here
urlpatterns = [
    path('', views.index, name='index'),
]
