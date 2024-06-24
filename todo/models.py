from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField()
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.content
