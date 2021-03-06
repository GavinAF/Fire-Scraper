# Generated by Django 2.2.4 on 2019-09-04 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, verbose_name='Link Url')),
                ('store', models.CharField(max_length=50, verbose_name='Store')),
                ('threshold', models.CharField(max_length=10)),
                ('active', models.CharField(default='True', max_length=6, verbose_name='Active (True/False)')),
                ('title', models.CharField(default='Product Name', max_length=100, verbose_name='Product name')),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
