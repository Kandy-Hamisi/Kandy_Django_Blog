from django.db import models
'''imported class models  '''
from django.contrib.auth.models import User


# Create your models here.

'''Declaring a tuple of a post to keep draft and published 
posts separated when we render them out with templates'''


STATUS = {
    (0,"Draft"),
    (1,"Publish")
}

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    

    '''we tell django to sort results in the created_on 
    field  '''
    class Meta:
        ordering = ['-created_on']

    '''default human-readable representation of the object '''
    def __str__(self):
        return self.title