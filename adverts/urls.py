from django.urls import path

from . import views

app_name = 'adverts'
urlpatterns = [
    path('', views.index, name='All'),
    path('<int:pk>', views.detail, name='detail'),

]
