from django.db import models

# Create your models here.
class ToDoItem(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    createdBy = models.CharField(max_length=250)
    status = models.CharField(max_length=50)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title