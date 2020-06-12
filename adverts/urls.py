from django.urls import path

from . import views

app_name = 'adverts'
urlpatterns = [
    path('', views.MainListView.as_view(), name='All'),
    path('<int:pk>', views.CategoryDetailView.as_view(), name='detail'),

]
