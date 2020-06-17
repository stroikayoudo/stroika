from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Category3, Category2, Category1, Banner
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .permissions import FollowerPermissionMixin
from .forms import AddBannerForm


class MainListView(generic.ListView):
    model = Category1
    template_name = 'adverts/main.html'

    def get_queryset(self):
        return Category1.objects.all()


class Category1DetailView(generic.DetailView):
    model = Category1
    template_name = 'adverts/detail.html'


class Category2DetailView(generic.DetailView):
    model = Category2
    template_name = 'adverts/detail2.html'


class Category3DetailView(generic.DetailView):
    model = Category3
    template_name = 'adverts/detail3.html'


class BannerDetailView(generic.DetailView):
    model = Banner
    template_name = 'adverts/banner.html'


class MyOrdersListView(generic.base.View):

    def get(self, request):
        return render(request, 'adverts/mybanners.html')


def add_banner_view(request):
    form = AddBannerForm(request.POST or None)
    if form.is_valid():
        print(form)
        fs = form.save(commit=False)
        fs.author = request.user
        fs.save()
        return redirect('/mybanners')

    context = {'form': form}
    return render(request, 'adverts/addbanner.html', context)


class BannerCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = AddBannerForm
    template_name = 'adverts/addbanner.html'
    success_url = '/mybanners'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BannerCreateView, self).form_valid(form)
