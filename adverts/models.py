from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.mail import send_mass_mail


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
    pub_time = models.DateTimeField('Дата публикации', default=timezone.now)
    price = models.IntegerField('Цена')
    amount = models.IntegerField('Количество')
    image = models.ImageField('Изображение', upload_to='adverts/', null=True)
    addition = models.TextField('Дополнительная информация')
    author = models.ForeignKey(User, related_name='mybanners', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def save(self, *args, **kwargs):
        datatuple = (
            ('Новое обьявление',
             'Посмотрите новое обьявление',
             'artemovanvar@gmail.com', [i.email]) for i in set([*self.category3.members.all(),
                                                                *self.category3.parent_category.members.all(),
                                                                *self.category3.parent_category.parent_category.members.all()]))
        send_mass_mail(datatuple)

        super().save(*args, **kwargs)


class Answer(models.Model):
    banner = models.ForeignKey(Banner, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(User, related_name='myanswers', on_delete=models.CASCADE, null=True)
    pub_time = models.DateTimeField('Дата публикации', default=timezone.now)
    text = models.TextField('Описание')

    def __str__(self):
        return self.author.username

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклик"


class Product1(models.Model):
    buyer = models.ForeignKey(User, related_name='myproducts1', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category1, on_delete=models.CASCADE, related_name='products')
    time = models.DateTimeField('Дата публикации', default=timezone.now)
    checked_out = models.BooleanField('Оплачено', default=False)

    def __str__(self):
        return self.buyer.username + ' ' + self.category

    class Meta:
        verbose_name = "Подписка на категорию 1"
        verbose_name_plural = "Подписки на категорию 1"


class Product2(models.Model):
    buyer = models.ForeignKey(User, related_name='myproducts2', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category2, on_delete=models.CASCADE, related_name='products')
    time = models.DateTimeField('Дата публикации', default=timezone.now)
    checked_out = models.BooleanField('Оплачено', default=False)

    def __str__(self):
        return self.buyer.username + ' ' + self.category

    class Meta:
        verbose_name = "Подписка на категорию 2"
        verbose_name_plural = "Подписки на категорию 2"


class Product3(models.Model):
    buyer = models.ForeignKey(User, related_name='myproducts3', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category3, on_delete=models.CASCADE, related_name='products')
    time = models.DateTimeField('Дата публикации', default=timezone.now)
    checked_out = models.BooleanField('Оплачено', default=False)

    def __str__(self):
        return self.buyer.username + ' ' + self.category

    class Meta:
        verbose_name = "Подписка на категорию 3"
        verbose_name_plural = "Подписки на категорию 3"
