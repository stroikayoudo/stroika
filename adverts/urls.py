from django.urls import path

from . import views

app_name = 'adverts'
urlpatterns = [
    path('', views.MainListView.as_view(), name='All'),
    path('<int:pk>', views.Category1DetailView.as_view(), name='detail'),
    path('category2/<int:pk>', views.Category2DetailView.as_view(), name='detail'),

]
