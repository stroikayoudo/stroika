from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Category3, Category2, Category1, Banner
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .permissions import FollowerPermissionMixin

class MainListView(generic.ListView):
    model = Category1
    template_name = 'adverts/index.html'

    def get_queryset(self):
        return Category1.objects.all()


class CategoryDetailView( generic.DetailView):
    model = Category2
    template_name = 'adverts/detail.html'

