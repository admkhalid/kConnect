from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    # date_posted = models.DateTimeField(auto_now = True) - update the date whenever the post is modified
    # date_posted = models.DateTimeField(auto_now_add = True) - keeps the date of the time when this object was created. 
    # doesn't let you change the date
    date_posted = models.DateTimeField(default=timezone.now) #now is a function. don't include the paranthesis, otherwise it'll execute.
    author = models.ForeignKey(User, on_delete = models.CASCADE) #on_delete = models.CASCADE deletes the post of the user is deleted
    
    #this prints the title of the object instead of the object id in the prompt 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})