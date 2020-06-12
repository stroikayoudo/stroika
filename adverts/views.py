from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Category3, Category2, Category1, Banner


class MainListView(generic.View):
    model = Category1
    template_name = 'adverts/index.html'

    def get_queryset(self):
        return Category1.objects.all()


def index(request):
    return render(request, 'adverts/index.html', {'categories': Category1.objects.all()})

def detail(request, pk):
    category = get_object_or_404(Category1, pk=pk)
    print(category.category2)
    return render(request, 'adverts/detail.html', {'category': category})
