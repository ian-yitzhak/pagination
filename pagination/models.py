from django.db import models





class Blog(models.Model):


    Title = models.CharField(max_length = 200)
    Content = models.CharField(max_length = 1000)
    Tag = models.CharField(max_length = 100)
    





    def __str__(self):

        return self.Title