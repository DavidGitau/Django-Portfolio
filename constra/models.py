import email
from django.db import models
from django.contrib.auth.models import User

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(default='Nats Stenman began his career in construction with boots on the ground')

    def __str__(self):
        return self.name
    
    class Meta:
        abstract = True
    
class Category(CommonInfo):
    about = None
    class Meta:
        verbose_name_plural = 'Categories'

class Comment(CommonInfo):
    post = models.ForeignKey('News', on_delete=models.CASCADE)
    n_name = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    website = models.URLField(null=True)


class Fact(CommonInfo):
    about = None
    number = models.IntegerField()
    image = models.ImageField(upload_to='images/icon-image/')

class News(CommonInfo):
    comments = models.IntegerField()
    comments_all = models.ManyToManyField(Comment)
    # author = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    image = models.ImageField(upload_to='images/news/')

    class Meta:
        verbose_name_plural = 'News'

class PricingFeatures(CommonInfo):
    pass

class Pricing(CommonInfo):
    about = None
    features = models.ManyToManyField(PricingFeatures)
    price = models.IntegerField()

class Project(CommonInfo):
    location = models.CharField(max_length=100, default='McLean, VA')
    client = models.CharField(max_length=100, default='Pransbay Powers Authority')
    architect = models.CharField(max_length=100, default='Dlarke Pelli Incorp')
    size = models.IntegerField()
    image = models.ImageField(upload_to='images/projects/')
    categories = models.ManyToManyField(Category)

class Service(CommonInfo):
    solutions = models.ManyToManyField('Solution')
    image1 = models.ImageField(upload_to='images/services/')
    image2 = models.ImageField(upload_to='images/services/')
    icon = models.ImageField(upload_to='images/services/')

class Solution(CommonInfo):
    about = None

class Team(CommonInfo):
    position = models.CharField(max_length=100, default='Innovation Officer')
    image = models.ImageField(upload_to='images/team/')

class Testimonial(CommonInfo):
    position = models.CharField(max_length=100, default='CEO, First Choice Group')
    image = models.ImageField(upload_to='images/clients/')
