from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=400, null=False)
    image = models.CharField(max_length=1000, null=False)
    slug = models.CharField(max_length=100, null=False, default='')

    def __str__(self):
        return str(self.name)


class Item(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=4000, blank=False, null=False)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.CharField(max_length=1000, null=False)
    price = models.FloatField(max_length=10, null=False, default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)

    class Meta:
        ordering = ['-update', 'created']

    def __str__(self):
        return str(self.name)


class ContactMessage(models.Model):
    username = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=100, null=False)
    message = models.CharField(max_length=4000, null=False)

    def __str__(self):
        return str(self.username)