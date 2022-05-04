from django.db import models

class Sity(models.Model):
    title = models.CharField("Name", max_length=50)
    description = models.TextField("Description")

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField("Name", max_length=100)
    sity = models.CharField("Sity", max_length=50)
    news = models.TextField("Description")

    def __str__(self):
        return self.title

class Place(models.Model):
    title = models.CharField("Name", max_length=50)
    description = models.TextField("Description")

    def __str__(self):
        return self.title

class Test_kz(models.Model):
    title = models.CharField("Name", max_length=50)
    description = models.TextField("Description")

    def __str__(self):
        return self.title