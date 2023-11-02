import uuid
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    theme = models.CharField(max_length=100, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.TextField()
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)

    def __str__(self):
        return self.theme

class Comment(models.Model):
    feedback = models.ForeignKey(Feedback, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, unique=True, editable=False)

