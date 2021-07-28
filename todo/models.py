from django.db import models

# Create your models here.
class TodoModel(models.Model):
  title = models.CharField(max_length=50)
  content = models.TextField()
  duedate = models.DateField()


def __str__(self):
  return self.title
