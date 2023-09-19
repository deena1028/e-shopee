# Generated by Django 4.2.5 on 2023-09-19 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catId', models.IntegerField(null=True)),
                ('catName', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='login1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=200)),
                ('paswod', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pId', models.IntegerField(null=True)),
                ('pName', models.TextField(max_length=200)),
                ('pdec', models.TextField(max_length=500)),
                ('pPrice', models.FloatField(max_length=200)),
                ('pQty', models.IntegerField(null=True)),
                ('catId', models.IntegerField(null=True)),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartId', models.IntegerField(null=True)),
                ('userId', models.TextField(max_length=100, null=True)),
                ('cartQty', models.IntegerField(null=True)),
                ('ppid', models.IntegerField(null=True)),
                ('pprice', models.IntegerField(null=True)),
                ('pname', models.TextField(max_length=200, null=True)),
                ('pcover', models.TextField(max_length=200, null=True)),
                ('tqty', models.IntegerField(null=True)),
                ('pId', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.product')),
            ],
        ),
    ]
