# Generated by Django 4.0.3 on 2022-08-20 20:23

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='Nats Stenman began his career in construction with boots on the ground')),
                ('email', models.EmailField(max_length=254)),
                ('website', models.URLField(null=True)),
                ('n_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/icon-image/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PricingFeatures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='Nats Stenman began his career in construction with boots on the ground')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='Nats Stenman began his career in construction with boots on the ground')),
                ('position', models.CharField(default='Innovation Officer', max_length=100)),
                ('image', models.ImageField(upload_to='images/team/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='Nats Stenman began his career in construction with boots on the ground')),
                ('position', models.CharField(default='CEO, First Choice Group', max_length=100)),
                ('image', models.ImageField(upload_to='images/clients/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='Nats Stenman began his career in construction with boots on the ground')),
                ('image1', models.ImageField(upload_to='images/services/')),
                ('image2', models.ImageField(upload_to='images/services/')),
                ('icon', models.ImageField(upload_to='images/services/')),
                ('solutions', models.ManyToManyField(to='constra.solution')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='Nats Stenman began his career in construction with boots on the ground')),
                ('location', models.CharField(default='McLean, VA', max_length=100)),
                ('client', models.CharField(default='Pransbay Powers Authority', max_length=100)),
                ('architect', models.CharField(default='Dlarke Pelli Incorp', max_length=100)),
                ('size', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/projects/')),
                ('categories', models.ManyToManyField(to='constra.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('features', models.ManyToManyField(to='constra.pricingfeatures')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.TextField(default='Nats Stenman began his career in construction with boots on the ground')),
                ('comments', models.IntegerField()),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='images/news/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comments_all', models.ManyToManyField(to='constra.comment')),
            ],
            options={
                'verbose_name_plural': 'News',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='constra.news'),
        ),
    ]
