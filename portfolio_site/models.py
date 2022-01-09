from django.db import models
from django.db.models.fields import BooleanField


# Create your models here.

class my_profile(models.Model):
    my_profile_status = models.BooleanField(default=False, null=True)
    my_full_name = models.CharField(max_length=100, blank=True, null=True)
    my_first_name = models.CharField(max_length=50, blank=True, null=True)
    my_middle_name = models.CharField(max_length=50, blank=True, null=True)
    my_last_name = models.CharField(max_length=50, blank=True, null=True)
    my_job_post = models.CharField(max_length=100, blank=True, null=True)
    my_about_me = models.TextField(max_length=5000, blank=True, null=True)
    my_email = models.EmailField(max_length=50, blank=True, null=True)
    my_email_alt = models.EmailField(max_length=50, blank=True, null=True)
    my_gender = models.CharField(max_length=25, blank=True, null=True)
    my_address = models.TextField(max_length=2000, blank=True, null=True)
    my_age = models.CharField(max_length=20, blank=True, null=True)
    my_profile_pic = models.ImageField(upload_to="admin_images")
    resume=models.FileField(upload_to="Resume")
    
    def __str__(self):
        return self.my_profile_status


class my_education(models.Model):
    active_status=BooleanField(default=False,null=False)
    edu_name = models.CharField(max_length=500, blank=True,null=True)
    edu_institute_name = models.CharField(max_length=500, blank=True,null=True)
    edu_date = models.CharField(max_length=100, blank=True,null=True)
    edu_description = models.TextField(max_length=3000, blank=True,null=True)
    edu_additional_info = models.TextField(max_length=100, blank=True,null=True)
    def __str__(self):
        return self.edu_name
    


class my_experience(models.Model):
    active_status=BooleanField(default=False,null=False)
    exp_name = models.CharField(max_length=500, blank=True,null=True)
    exp_org_name = models.CharField(max_length=500, blank=True,null=True)
    exp_date = models.CharField(max_length=100, blank=True,null=True)
    exp_description = models.TextField(max_length=3000, blank=True,null=True)
    exp_additional_info = models.TextField(max_length=100, blank=True,null=True)
    exp_letter_link = models.URLField(max_length=300,blank=True,null=True)

    def __str__(self):
        return self.exp_name
    

# Create your models here.
class certification(models.Model):
    active_status=BooleanField(default=False,null=False)
    certificate_file=models.FileField(upload_to="adminfiles")
    certificate_name = models.CharField(max_length=500, blank=True,null=True)
    certificate_org_name = models.CharField(max_length=500, blank=True,null=True)
    certificate_date = models.CharField(max_length=500, blank=True,null=True)
    certificate_description=models.TextField(max_length=1000,blank=True,null=True)
    certificate_link=models.URLField(max_length=300,blank=True,null=True)
    def __str__(self):
        return self.certificate_name
    
class Blog(models.Model):
    active_status=BooleanField(default=False,null=False)
    blog_title=models.CharField(max_length=500, blank=True,null=True)
    blog_image=models.ImageField(upload_to="blog_images")
    blog_description=models.CharField(max_length=500, blank=True,null=True)
    publish_time=models.CharField(max_length=500, blank=True,null=True)
    blog_subject=models.CharField(max_length=500,blank=True,null=True)
    def __str__(self):
        return self.blog_title
    
class Project(models.Model):
    active_status=BooleanField(default=False,null=False)
    project_title=models.CharField(max_length=500, blank=True,null=True)
    project_url=models.URLField(max_length=100,blank=True,null=True)
    project_code=models.URLField(max_length=100,blank=True,null=True)
    project_image=models.ImageField(upload_to="project_images")
    project_description=models.CharField(max_length=500, blank=True,null=True)
    project_published_date=models.CharField(max_length=500, blank=True,null=True)
    def __str__(self):
        return self.project_title
    
class Skill(models.Model):
    active_status=BooleanField(default=False,null=False)
    skillname=models.CharField(max_length=100, blank=True,null=True)
    skillpercentage=models.IntegerField(max_length=100,blank=True,null=True)
    def __str__(self):
        return self.skillname
    