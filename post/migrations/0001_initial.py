# Generated by Django 2.2.7 on 2019-11-24 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('live_link', models.URLField()),
                ('description', models.TextField()),
                ('country', django_countries.fields.CountryField(max_length=746, multiple=True)),
                ('languages', multiselectfield.db.fields.MultiSelectField(choices=[('Django', 'Django'), ('Flask', 'Flask'), ('Python', 'Python'), ('Bootstrap', 'Bootstrap'), ('Material-Design', 'Material-Design'), ('Angular', 'Angular'), ('Html', 'Html'), ('Java-Script', 'Java-Script'), ('Java', 'Java'), ('Ruby', 'Ruby')], max_length=80)),
                ('landing_page', models.ImageField(upload_to='media/images')),
                ('screenshot_one', models.ImageField(upload_to='media/images')),
                ('screenshot_two', models.ImageField(upload_to='media/images')),
                ('screenshot_three', models.ImageField(upload_to='media/images')),
                ('screenshot_four', models.ImageField(upload_to='media/images')),
                ('date_posted', models.DateField(auto_now_add=True)),
                ('profile_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('design', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('usability', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('content', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-id'],
                'unique_together': {('user', 'design', 'usability', 'content', 'post')},
                'index_together': {('user', 'design', 'usability', 'content', 'post')},
            },
        ),
    ]
