# Generated by Django 3.0.3 on 2020-06-14 09:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0004_auto_20200614_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='category3',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='banner', to='adverts.Category3'),
            preserve_default=False,
        ),
    ]