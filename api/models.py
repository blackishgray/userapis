from django.db import models

# Create your models here.
class UserApiModel(models.Model):
    first_name = models.TextField(max_length=200)
    last_name = models.TextField(max_length=200)
    email = models.EmailField(max_length=200)
    age = models.IntegerField(null=True)
    dob = models.DateField(blank=True)
    mobile_no = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
