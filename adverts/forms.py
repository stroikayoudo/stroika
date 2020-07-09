from django import forms
from .models import Banner, Product3, Product2, Product1


class AddBannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['category3',
                  'title',
                  'description',
                  'price',
                  'amount',
                  'addition',
                  'image']


class Product1Form(forms.ModelForm):
    class Meta:
        model = Product1
        fields = ['category']


class Product2Form(forms.ModelForm):
    class Meta:
        model = Product2
        fields = ['category']


class Product3Form(forms.ModelForm):
    class Meta:
        model = Product3
        fields = ['category']
