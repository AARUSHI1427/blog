from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(null=True,blank=True)
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True,auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail",kwargs={"id":self.id})

    class Meta:
        ordering = ["-timestamp","-updated"]
