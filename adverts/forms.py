from django import forms
from .models import Banner, Answer


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


