# Generated by Django 5.0 on 2024-04-27 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=24)),
                ('password', models.CharField(max_length=126)),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('productid', models.IntegerField()),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('orderid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=56)),
                ('state', models.CharField(max_length=56)),
                ('description', models.TextField()),
                ('mode_of_payment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('image', models.ImageField(upload_to='images')),
                ('price', models.IntegerField()),
                ('categoryid', models.IntegerField()),
                ('detail', models.TextField()),
                ('product_code', models.CharField(max_length=56)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=56)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=56)),
                ('password', models.CharField(max_length=126)),
            ],
        ),
    ]
