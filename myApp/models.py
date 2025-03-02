"""
This file contains all the database tables.
"""
from django.db import models

# Create your models here.
class Details(models.Model):
    """
    Stores name, age, email, remark, is_detail in the Details table.
    The is_delete field is for soft delete.
    """
    name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    remark = models.TextField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name)
