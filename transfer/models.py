from django.contrib.admin import options
from django.db import models

# Create your models here.
class C_details(models.Model):
    c_id = models.IntegerField(unique=True)
    c_name = models.CharField(max_length=122)
    c_email = models.CharField(max_length=122)
    c_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.c_name

class C_history(models.Model):
    s_id = models.IntegerField()
    s_name = models.CharField(max_length=122)
    r_id = models.IntegerField()
    r_name = models.CharField(max_length=122)
    t_date = models.DateTimeField()
    transaction = models.IntegerField()


    