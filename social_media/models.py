from django.db import models
from social_media.utils import TimeStamped

class Post(TimeStamped):
    name = models.CharField(max_length=500, null=True, blank=True)
    category = models.CharField(max_length=500, null=True, blank=True)
    founder = models.CharField(max_length=500, null=True, blank=True)
    image = models.TextField(default='n/a')
    description = models.TextField(default='n/a')


    def __str__(self):
        return f"{self.name} - {self.founder}"
    
    class Meta:
        verbose_name_plural = 'Recipe'