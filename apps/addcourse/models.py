from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=45, blank=False, null=False)
    description = models.TextField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     managed = False
    #     db_table = 'Courses'
