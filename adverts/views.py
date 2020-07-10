from django.views import generic
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, send_mass_mail
from django.http import HttpResponseRedirect, JsonResponse, Http404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Category3, Category2, Category1, Banner, Product1, Product2, Product3
from .permissions import FollowerPermissionMixin
from .forms import AddBannerForm, Product1Form, Product2Form, Product3Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import json

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


class BannerDetailView(FollowerPermissionMixin, generic.DetailView):
    model = Banner
    template_name = 'adverts/banner.html'


class MyOrdersListView(generic.base.View):

    def get(self, request):
        return render(request, 'adverts/mybanners.html')


class BannerCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = AddBannerForm
    template_name = 'adverts/addbanner.html'
    success_url = '/mybanners'

    def get(self, request, *args, **kwargs):
        self.object = None
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        if kwargs['pk']:
            kwargs['form'].initial['category3'] = get_object_or_404(Category3, pk=kwargs['pk'])
            kwargs['form'].instance.category3 = get_object_or_404(Category3, pk=kwargs['pk'])

        return self.render_to_response(self.get_context_data(**kwargs))

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(BannerCreateView, self).form_valid(form)


def leave_answer(request, banner_id):
    banner = get_object_or_404(Banner, pk=banner_id)
    banner.answers.create(author=request.user, text=request.POST['text'])
    send_mail(
        'У вас новый ответ',
        f'Кто то оставил ответ на ваше обьявление {banner.title}',
        'artemovanvar@gmail.com',
        [banner.author.email])
    return HttpResponseRedirect(reverse('adverts:banner_detail',
                                        args=(banner.category3.parent_category.parent_category.id,
                                              banner.category3.parent_category.id,
                                              banner.category3.id,
                                              banner.id)))


def products(request):
    return render(request, 'adverts/products.html')


class ProductListView(generic.base.View):

    def get(self, request):
        return render(request, 'adverts/mybanners.html')


@login_required
def product(request, pk):
    if pk == 1:
        form = Product1Form
        price = '20'
    elif pk == 2:
        form = Product2Form
        price = '30'
    elif pk == 3:
        form = Product3Form
        price = '40'
    else:
        return Http404("Product does not exist")
    return render(request,
                  'adverts/product.html',
                  context={'form': form, 'price': price, 'prodId': pk})


def paymentComplete(request):
    body = json.loads(request.body)

    pk = int(body['selected'])
    if body['productId'] == '1':
        category = get_object_or_404(Category1, pk=pk)
    elif body['productId'] == '2':
        category = get_object_or_404(Category2, pk=pk)
    elif body['productId'] == '3':
        category = get_object_or_404(Category3, pk=pk)
    else:
        return Http404("Payment doesn't exist")

    category.members.add(User.objects.get(id=int(body['userId'])))

    return JsonResponse('Payment completed!', safe=False)
