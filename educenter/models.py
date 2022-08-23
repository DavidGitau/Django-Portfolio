from django.db import models

# Create your models here.
from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=100, null=False)
    content = models.TextField(default='')
    header_about = models.ForeignKey('About', null=True, on_delete=models.CASCADE)
    class Meta:
        abstract = True
        ordering = ['id']

    def __str__(self):
        return self.name

class About(CommonInfo):
    header_about = None
    model_name = models.CharField(max_length=100,default='about')

class Blog(CommonInfo):
    name = None
    author = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField()
    post_read = models.IntegerField()
    post_share = models.IntegerField()
    post_comments = models.IntegerField()
    heading = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='images/blog/', null=True)
    model_name = models.CharField(max_length=100,default='blog')
    class Meta:
        ordering = ['heading']
        
    def __str__(self):
        return self.heading

class Course(CommonInfo):
    c_length = models.IntegerField()
    c_duration = models.IntegerField()
    c_requirement = models.ManyToManyField('Requirement')
    c_teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    c_school = models.ForeignKey('School', on_delete=models.CASCADE)
    fees = models.FloatField(null=True, blank=True)
    funding = models.TextField(null=True, blank=True) 
    image_url = models.ImageField(upload_to='images/courses/', null=True)
    model_name = models.CharField(max_length=100,default='course')

class Event(CommonInfo):
    location = models.CharField(max_length=255)
    event_date = models.DateField()
    event_time = models.TimeField()
    e_speaker = models.ManyToManyField('Teacher')
    fee = models.IntegerField()
    image_url = models.ImageField(upload_to='images/events/', null=True)
    model_name = models.CharField(max_length=100,default='event')

class FunFact(CommonInfo):
    content = None
    number = models.IntegerField()
    model_name = models.CharField(max_length=100,default='funfact')

class Interest(CommonInfo):
    content = None
    model_name = models.CharField(max_length=100,default='interest')

class Notice(CommonInfo):
    notice_date = models.DateField()
    model_name = models.CharField(max_length=100,default='notice')

class Requirement(CommonInfo):
    content = None
    model_name = models.CharField(max_length=100,default='requirement')

class Research(CommonInfo):
    image_url = models.ImageField(upload_to='images/research/', null=True)
    model_name = models.CharField(max_length=100,default='research')

class School(CommonInfo):
    content = None
    header_about = None
    model_name = models.CharField(max_length=100,default='school')

class Scholarship(CommonInfo):
    content = None
    s_course = models.ForeignKey('School', null=True, on_delete=models.CASCADE)
    s_requirement = models.ManyToManyField('Requirement')
    image_url = models.ImageField(upload_to='images/scholarship/', null=True)
    model_name = models.CharField(max_length=100,default='scholarship')

class Teacher(CommonInfo):
    education = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    t_interest = models.ManyToManyField('Interest')
    email = models.EmailField(default='default@ex.co.ke')
    phone = models.CharField(max_length=50, default='+254 700 000 000')
    social_media = models.CharField(max_length=50, default='default')
    address = models.CharField(max_length=100, default='Default, Setting')
    t_courses = models.ManyToManyField('Course')
    image_url = models.ImageField(upload_to='images/teachers/', null=True)
    model_name = models.CharField(max_length=100,default='teacher')