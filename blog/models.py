from django.db import models


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
