from django.db import models

# Create your models here.
class Details(models.Model):
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    remark = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name