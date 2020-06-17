from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category1(models.Model):
    """Категория 1"""
    name = models.CharField("Категория 1", max_length=150)
    description = models.TextField("Описание")
    members = models.ManyToManyField(User, related_name='members1', blank=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория 1"
        verbose_name_plural = "Категории 1"


class Category2(models.Model):
    """Категория 2"""
    parent_category = models.ForeignKey(Category1, on_delete=models.CASCADE, related_name='category2')
    name = models.CharField("Категория 2", max_length=150)
    description = models.TextField("Описание")
    members = models.ManyToManyField(User, related_name='members2', blank=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория 2"
        verbose_name_plural = "Категории 2"


class Category3(models.Model):
    """Категория 3"""
    parent_category = models.ForeignKey(Category2, on_delete=models.CASCADE, related_name='category3')
    name = models.CharField("Категория 3", max_length=150)
    description = models.TextField("Описание")
    members = models.ManyToManyField(User, related_name='members3', blank=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория 3"
        verbose_name_plural = "Категории 3"


class Banner(models.Model):
    """Объявление"""
    category3 = models.ForeignKey(Category3, on_delete=models.CASCADE, related_name='banner')
    title = models.CharField("Наименование", max_length=150)
    description = models.TextField('Описание')
    pub_time = models.DateTimeField('Дата публикации', default=timezone.now())
    price = models.IntegerField('Цена')
    amount = models.IntegerField('Количество')
    image = models.ImageField('Изображение', upload_to='adverts/')
    addition = models.TextField('Дополнительная информация')
    author = models.ForeignKey(User, related_name='mybanners', on_delete=models.CASCADE)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
