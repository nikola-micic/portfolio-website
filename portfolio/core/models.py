from django.db import models

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.TextField()
    project_img = models.ImageField(upload_to='static/images/')
    project_link = models.URLField()

    def __str__(self):
        return self.project_name

