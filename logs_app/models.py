from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model) :
    text = models.CharField(max_length=200)
    add_date = models.DateTimeField(auto_now_add=True)
    owner =models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) :
        return self.text


class Entry(models.Model) :
    refrence = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta :
        verbose_name_plural = "Entries"

    def __str__(self) :
        if len(self.text) <= 50 :
            return self.text
        else :
            return f"{self.text[:50]}..."