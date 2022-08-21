from django.db import models


class ProjectType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    project_type  = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/portfolio')
    year = models.DateField()
    client = models.CharField(max_length=100)
    about = models.TextField(
        default="""
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Commodi eligendi fugiat ad cupiditate hic, eum debitis ipsum, quos non mollitia. Commodi suscipit obcaecati et, aperiam quas vero quo, labore tempore.

Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aperiam debitis beatae doloremque cupiditate vel repellat nam est voluptates, magnam quod explicabo fugit, quidem.
        """)

    def __str__(self):
        return self.name
