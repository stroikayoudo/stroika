from django.urls import path

from . import views

app_name = 'adverts'
urlpatterns = [
    path('', views.MainListView.as_view(), name='all'),
    path('category1/<int:pk>', views.Category1DetailView.as_view(), name='detail'),
    path('category1/<int:category1_id>/category2/<int:pk>', views.Category2DetailView.as_view(), name='detail2'),
    path('category1/<int:category1_id>/category2/<int:category2_id>/category3/<int:pk>',
         views.Category3DetailView.as_view(), name='detail3'),
    path('category1/<int:category1_id>/category2/<int:category2_id>/category3/<int:category3_id>/banner/<int:pk>',
         views.BannerDetailView.as_view(), name='banner_detail'),
    path('mybanners/', views.MyOrdersListView.as_view(), name='mybanners'),
    path('addbanner/', views.BannerCreateView.as_view(), name='addbanner'),
    path('leave_answer/<int:banner_id>', views.leave_answer, name='leave_answer'),

]
