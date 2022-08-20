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

class Blog(CommonInfo):
    name = None
    author = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    post_date = models.DateField()
    post_read = models.IntegerField()
    post_share = models.IntegerField()
    post_comments = models.IntegerField()
    heading = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='images/blog/', null=True)
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

class Event(CommonInfo):
    location = models.CharField(max_length=255)
    event_date = models.DateField()
    event_time = models.TimeField()
    e_speaker = models.ManyToManyField('Teacher')
    fee = models.IntegerField()
    image_url = models.ImageField(upload_to='images/events/', null=True)

class FunFact(CommonInfo):
    content = None
    number = models.IntegerField()

class Interest(CommonInfo):
    content = None

class Notice(CommonInfo):
    notice_date = models.DateField()

class Requirement(CommonInfo):
    content = None

class Research(CommonInfo):
    image_url = models.ImageField(upload_to='images/research/', null=True)

class School(CommonInfo):
    content = None
    header_about = None

class Scholarship(CommonInfo):
    content = None
    s_course = models.ForeignKey('School', null=True, on_delete=models.CASCADE)
    s_requirement = models.ManyToManyField('Requirement')
    image_url = models.ImageField(upload_to='images/scholarship/', null=True)

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