# Generated by Django 4.0 on 2022-01-09 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(blank=True, max_length=500, null=True)),
                ('blog_image', models.ImageField(upload_to='blog_images')),
                ('blog_description', models.CharField(blank=True, max_length=500, null=True)),
                ('publish_time', models.CharField(blank=True, max_length=500, null=True)),
                ('blog_subject', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_file', models.FileField(upload_to='adminfiles')),
                ('certificate_name', models.CharField(blank=True, max_length=500, null=True)),
                ('certificate_org_name', models.CharField(blank=True, max_length=500, null=True)),
                ('certificate_date', models.CharField(blank=True, max_length=500, null=True)),
                ('certificate_description', models.TextField(blank=True, max_length=1000, null=True)),
                ('certificate_link', models.URLField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='my_education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edu_name', models.CharField(blank=True, max_length=500, null=True)),
                ('edu_institute_name', models.CharField(blank=True, max_length=500, null=True)),
                ('edu_date', models.CharField(blank=True, max_length=100, null=True)),
                ('edu_description', models.TextField(blank=True, max_length=3000, null=True)),
                ('edu_additional_info', models.TextField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='my_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_name', models.CharField(blank=True, max_length=500, null=True)),
                ('exp_org_name', models.CharField(blank=True, max_length=500, null=True)),
                ('exp_date', models.CharField(blank=True, max_length=100, null=True)),
                ('exp_description', models.TextField(blank=True, max_length=3000, null=True)),
                ('exp_additional_info', models.TextField(blank=True, max_length=100, null=True)),
                ('exp_letter_link', models.URLField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='my_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_profile_status', models.BooleanField(default=False, null=True)),
                ('my_full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('my_first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('my_middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('my_last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('my_job_post', models.CharField(blank=True, max_length=100, null=True)),
                ('my_about_me', models.TextField(blank=True, max_length=5000, null=True)),
                ('my_email', models.EmailField(blank=True, max_length=50, null=True)),
                ('my_email_alt', models.EmailField(blank=True, max_length=50, null=True)),
                ('my_gender', models.CharField(blank=True, max_length=25, null=True)),
                ('my_address', models.TextField(blank=True, max_length=2000, null=True)),
                ('my_age', models.CharField(blank=True, max_length=20, null=True)),
                ('my_profile_pic', models.ImageField(upload_to='admin_images')),
                ('resume', models.FileField(upload_to='Resume')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(blank=True, max_length=500, null=True)),
                ('project_url', models.URLField(blank=True, max_length=100, null=True)),
                ('project_code', models.URLField(blank=True, max_length=100, null=True)),
                ('project_image', models.ImageField(upload_to='project_images')),
                ('project_description', models.CharField(blank=True, max_length=500, null=True)),
                ('project_published_date', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillname', models.CharField(blank=True, max_length=100, null=True)),
                ('skillpercentage', models.IntegerField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
